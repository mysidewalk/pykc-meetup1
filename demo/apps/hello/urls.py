""" Urls for hello app
"""
from rest_framework import routers

from hello import views as hello_views

router = routers.DefaultRouter(trailing_slash=False)
router.register('greetings', hello_views.GreetingViewSet)

urlpatterns = router.urls
