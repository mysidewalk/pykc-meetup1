""" Base urls for demo project
"""
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.http import HttpResponse


class IndexView(TemplateView):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello world, please browse to /admin to see api admin.')


admin.autodiscover()
urlpatterns = patterns(
    '',
    url(r'^admin', include(admin.site.urls)),
    url(r'^((?!admin|api|docs).)*$', IndexView.as_view()),
)

urlpatterns += patterns(
    '',
    # KICKSTARTER: DRF doesn't properly support namespaces, making '^api/' necessary before each
    url(r'^api/hello', include('hello.urls')),
)
