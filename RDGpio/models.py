from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class GPIO(models.Model):
    pin = models.IntegerField()
    conf = models.BooleanField(default=False)
    state = models.BooleanField(editable=False)
    
