""" Viewsets for hello app
"""
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin

from soakinspecks import models as ss_models
from soakinspecks import serializers as ss_serializers


class FlavorViewset(ModelViewSet):
    model = ss_models.Flavor


class OrderViewset(GenericViewSet, 
                   RetrieveModelMixin, ListModelMixin,
                   CreateModelMixin, DestroyModelMixin):
    model = ss_models.Order


class InventoryViewset(GenericViewSet,
                       RetrieveModelMixin, ListModelMixin):
    model = ss_models.Inventory


class MixturePartViewset(GenericViewSet,
                         RetrieveModelMixin, ListModelMixin,
                         CreateModelMixin, DestroyModelMixin):
    model = ss_models.MixturePart
    ss_serializers.MixturePartSerializer


class MixtureViewset(GenericViewSet,
                     RetrieveModelMixin, ListModelMixin, 
                     CreateModelMixin):
    model = ss_models.Mixture
    serializer_class = ss_serializers.MixtureSerializer


class ProductionBatchViewSet(GenericViewSet,
                             CreateModelMixin):
    model = ss_models.ProductionBatch
    serializer_class = ss_serializers.ProductionBatchSerializer
    

class OrderProcessBatchViewSet(GenericViewSet,
                               CreateModelMixin):
    model = ss_models.OrderProcessBatch

