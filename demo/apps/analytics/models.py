""" Models for the 'analytics' app
"""
import httplib

from django.db import models
from django.conf import settings
from django.contrib.contenttypes import generic, models as ct_models


class ContentView(models.Model):
    """ Tracks instances that content was delivered/viewed.
    """
    _format = u'{} {}: by: {}, at: {}, content_type: {}, content_id: {}, path: {}, referer: {}'
    
    content_type = models.ForeignKey(ct_models.ContentType)
    object_id = models.BigIntegerField()
    content_object = generic.GenericForeignKey()
    status = models.IntegerField(choices=httplib.responses.items())
    path = models.CharField(max_length=200)
    referer = models.CharField(max_length=200)
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    requested_at = models.DateTimeField()
    
    def __unicode__(self):
        return self._format.format(
            type(self).__name__,
            self.id,
            self.requested_by_id,
            self.requested_at,
            self.content_type_id,
            self.object_id,
            self.path,
            self.referer,
        )
