""" Admin configuration for the analytics app
"""
from django.contrib import admin

from analytics.models import ContentView


class ContentViewAdmin(admin.ModelAdmin):
    readonly_fields = ContentView._meta.get_all_field_names()
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(ContentView, ContentViewAdmin)
