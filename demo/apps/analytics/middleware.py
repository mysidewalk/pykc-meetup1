""" Middleware for the analytics app
"""
import logging

from django.contrib.contenttypes import models as ct_models
from django.utils import timezone

from analytics.models import ContentView

class ContentViewMiddleware(object):
    _active_methods = {
        'GET',
        'HEAD',
    }
    
    def handle_content_views(self, user_id, content_type_id, object_ids, status, path, referer):
        requested_at = timezone.now()
        content_views = ContentView.objects.bulk_create(
            ContentView(
                requested_by_id=user_id,
                requested_at=requested_at,
                content_type_id=content_type_id,
                object_id=object_id,
                status=status,
                path=path,
                referer=referer,
            )
            for object_id in object_ids
        )

    def process_response(self, request, response):
        if request.method in self._active_methods:
            user_id = request.user.id
            model = request.model
            if model:
                content_type = ct_models.ContentType.objects.get_for_model(model)
                data = getattr(response, 'data', {'id': -1})
                status = response.status_code
                path = request.path_info
                referer = request.META.get('HTTP_REFERER', '')
                if hasattr(data, 'keys'):
                    data = [data, ]
                object_ids = [item.get('id') for item in data if 'id' in item]
                self.handle_content_views(user_id, content_type.id, object_ids, status, path, referer)
        return response
