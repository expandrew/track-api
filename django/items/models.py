from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField

class Item(models.Model):
    PRIVACY_LEVELS = (
        ('1', 'Public'),
        ('2', 'Semi-Public'),
        ('3', 'Semi-Private'),
        ('4', 'Private')
    )

    item_type = models.CharField(max_length=64)
    privacy = models.CharField(max_length=1, choices=PRIVACY_LEVELS)
    data = JSONField()
