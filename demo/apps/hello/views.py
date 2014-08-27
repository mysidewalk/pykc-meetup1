""" Viewsets for hello app
"""
from rest_framework.viewsets import ModelViewSet

from hello.models import Greeting


class GreetingViewSet(ModelViewSet):
    model = Greeting

