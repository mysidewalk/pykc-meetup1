""" Models for the 'soakinspecks' app
"""
import itertools

from django.db import models, transaction
from django.core.exceptions import ValidationError


class Flavor(models.Model):
    """ Represents a flavor of the always delicious, always futuristic, soakin' specs!
    """
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    in_production = models.BooleanField()
    
    def __unicode__(self):
        return '#{} - {}, in production? {}'.format(
            self.id,
            self.title,
            self.in_production and 'Yes' or 'No',
        )

class MixturePart(models.Model):
    """ Represents a part of a mixture recipe
    """
    mixture = models.ForeignKey('soakinspecks.Mixture', related_name='parts')
    flavor = models.ForeignKey('soakinspecks.Flavor', related_name='mixture_participations')
    parts = models.PositiveIntegerField()


class Mixture(models.Model):
    """ Represents a unique mixture of flavors
    """
    title = models.CharField(max_length=200)
    
    @property
    def all_parts_available(self):
        return all(part.in_production for part in self.parts)


class AbstractInventory(models.Model):
    """ Abstract base for inventory containing common fields and methods 
    """
    mixture = models.OneToOneField('soakinspecks.Mixture', null=True, blank=True)
    flavor = models.OneToOneField('soakinspecks.Flavor', null=True, blank=True)
    quantity = models.PositiveIntegerField()

    @property
    def still_in_production(self):
        """ Tests if a mixture or flavor can be restocked
        """
        if self.mixture_id:
            result = self.mixture.all_parts_available
        elif self.flavor_id:
            result = self.flavor.in_production
        else:
            result = False
        return result
    
    def clean(self):
        """ Ensures that this model has a link to one and only one flavor/mixture
        """
        super(AbstractInventory, self).clean()
        if bool(self.mixture_id) == bool(self.flavor_id):
            raise ValidationError('Inventory *must* point to a mixture *or* a flavor.')
    
    def __unicode__(self):
        return '{} - mixture: {}, flavor {}, quantity: {}'.format(
            self.id,
            self.mixture_id,
            self.flavor_id,
            self.quantity,
        )
    
    class Meta(object):
        abstract = True


class Inventory(AbstractInventory):
    """ Represents available inventory of flavors and mixtures.
    """
    pass


class Order(models.Model):
    """ Represents an order in the system against an inventory line.
        It can be fulfilled, rainchecked, or impossible to fulfill.
    """
    inventory = models.ForeignKey('soakinspecks.Inventory', related_name='orders')
    customer_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price_quote = models.DecimalField(max_digits=10, decimal_places=2)
    is_fulfilled = models.BooleanField(default=False)
    is_rainchecked = models.BooleanField(default=False)
    is_impossible = models.BooleanField(default=False)
    
    @property
    def unit_price(self):
        """ Cost per unit of an order
        """
        return self.price_quote / self.quantity
    
    @classmethod
    def fill_orders(cls, orders):
        """ Fills orders per inventory item they are linked to, rainchecked first and by best
            unit price.
        """
        sorted_orders = sorted(
            orders,
            key=lambda x: (x.inventory, not x.is_rainchecked, x.unit_price),
        )
        grouped_orders = [
            (inventory, list(orders))
            for inventory, orders in itertools.groupby(sorted_orders, key=lambda x: x.inventory)
        ]
        with transaction.atomic():
            for inventory, orders in grouped_orders:
                for order in orders:
                    if order.can_fulfill:
                        order.fulfill()
                    elif inventory.still_in_production:
                        order.raincheck()
                    else:
                        order.impossible()
    
    @property
    def can_fulfill(self):
        """ Determines if an order can be fulfilled currently
        """
        return self.inventory.quantity > self.quantity
    
    def fulfill(self):
        """ Fulfills the order
        """
        assert not any((self.is_fulfilled, self.is_impossible)),\
            'This order cannot be fulfill-ed.'
        inventory = self.inventory
        inventory.quantity -= self.quantity
        inventory.save()
        self.is_fulfilled = True
        self.is_rainchecked = False
        self.save()
        
    def raincheck(self):
        """ Rainchecks the order
        """
        assert not any((self.is_fulfilled, self.is_rainchecked, self.is_impossible)),\
            'This order cannot be raincheck-ed.'
        self.is_rainchecked = True
        self.save()
        
    def impossible(self):
        """ Marks Impossible the order
        """
        assert not any((self.is_fulfilled, self.is_rainchecked, self.is_impossible)),\
            'This order cannot be impossible-ed.'
        self.is_impossible = True
        self.save()
        
    def __unicode__(self):
        return '{} - inventory: {}, customer: {}, quantity: {}, unit_price {}'.format(
            self.id,
            self.inventory_id,
            self.customer_name,
            self.quantity,
            self.unit_price,
        )


class ProductionBatch(AbstractInventory):
    """ Represents a batch of product that has been produced, persisted through other models.
    """
    
    def full_clean(self, exclude=None, validate_unique=True):
        return super(AbstractInventory, self).full_clean(None, False)
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        matching_inventory = Inventory.objects.filter(
            mixture=self.mixture,
            flavor=self.flavor
        ).first()
        if matching_inventory:
            matching_inventory.quantity += self.quantity
            matching_inventory.save()
        else:
            Inventory.objects.create(
                mixture=self.mixture,
                flavor=self.flavor,
                quantity=self.quantity,
            )
    
    class Meta(object):
        managed = False


class OrderProcessBatch(models.Model):
    """ Represents a batch of order processing. Not persisted.
    """
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        with transaction.atomic():
            orders = Order.objects\
                .filter(is_fulfilled=False, is_impossible=False)\
                .order_by('inventory', '-is_rainchecked', '-price_quote', 'quantity')
            Order.fill_orders(orders)

    class Meta(object):
        managed = False

