""" Common middleware items
"""
from django.core import urlresolvers


class APIRequestMetadataMiddleware(object):
    """ Adds model and viewset to request objects
    """
    
    @staticmethod
    def resolve_request(request):
        try:
            resolver_match = urlresolvers.resolve(request.path_info)
            func = resolver_match.func
            viewset = func.cls
            model = viewset.model
        except:
            viewset, model = None, None
        return viewset, model
    
    def process_request(self, request):
        viewset, model = self.resolve_request(request)
        request.model = model
        request.viewset = viewset

