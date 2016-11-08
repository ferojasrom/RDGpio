from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class GPIOs(models.Model):
    pin = models.IntegerField(default=0)
    conf = models.BooleanField(default=False)
    state = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return str(self.pin)
