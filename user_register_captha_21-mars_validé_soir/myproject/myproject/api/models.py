# -*- coding: utf-8 -*-

# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=32)
    firstName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=256)


