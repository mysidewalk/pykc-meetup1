""" Base urls for demo project
"""
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.http import HttpResponse


class IndexView(TemplateView):
    _format = 'Hello world, please browse to <a href="{}">admin</a> or <a href="{}">docs</a>.'

    def get(self, request, *args, **kwargs):
        admin_href = '/admin'
        docs_href = '/docs'
        response_body = self._format.format(admin_href, docs_href)
        return HttpResponse(response_body)


admin.autodiscover()
urlpatterns = patterns(
    '',
    url(r'^admin', include(admin.site.urls)),
    url(r'^docs', include('rest_framework_swagger.urls')),
    url(r'^((?!admin|api|docs).)*$', IndexView.as_view()),
)

urlpatterns += patterns(
    '',
    # KICKSTARTER: DRF doesn't properly support namespaces, making '^api/' necessary before each
    url(r'^api/hello', include('hello.urls')),
    url(r'^api/soakinspecks', include('soakinspecks.urls')),
)
