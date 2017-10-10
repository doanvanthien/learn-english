# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class words(models.Model):
	en = models.CharField(max_length=100)
	vi = models.CharField(max_length=100)
	state = models.IntegerField(max_length=1)
	categories = models.CharField(max_length=50)

class modules(models.Model):
	module_name = models.CharField(max_length=100)
	hash_value = models.CharField(max_length=100)
