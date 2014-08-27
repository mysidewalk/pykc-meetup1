""" Models for the 'hello' app
"""
from collections import OrderedDict

from django.db import models


class Salutations(object):
    HELLO = 'HELLO'
    HIYA = 'HIYA'
    WHATSUP = 'WHATSUP'
    YO = 'YO'
    mapping = OrderedDict([
        (HELLO, 'Hello'),
        (HIYA, 'Hiya'),
        (WHATSUP, "What's up"),
        (YO, 'Yo'),
    ])
    choices = mapping.items()


class Greeting(models.Model):
    salutation = models.CharField(max_length=20, choices=Salutations.choices)
    subject = models.CharField(max_length=50)
    
    def __unicode__(self):
        return '{}, {}!'.format(Salutations.mapping[self.salutation], self.subject)

