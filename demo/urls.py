""" Base urls for demo project
"""
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.http import HttpResponse


class HubView(TemplateView):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello world!')


admin.autodiscover()
urlpatterns = patterns(
    '',
    url(r'^api/hello/', include('hello.urls', namespace='hello')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^((?!api|docs).)*$', HubView.as_view()),
)