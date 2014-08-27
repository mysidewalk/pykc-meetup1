""" Models for the 'hello' app
"""
from django.db import models


class Greeting(models.Model):
    subject = models.CharField(max_length=50)

