from __future__ import unicode_literals

from django.utils import timezone

from django.db import models
from django.contrib.postgres.fields import JSONField

class Item(models.Model):
    PRIVACY_LEVELS = (
        ('1', '[1] Public'),
        ('2', '[2] Semi-Public'),
        ('3', '[3] Semi-Private'),
        ('4', '[4] Private')
    )

    ITEM_TYPES = (
        ('note', 'Note'),
        ('bookmark', 'Bookmark')
    )

    item_type = models.CharField('Item Type', max_length=64, choices=ITEM_TYPES)
    privacy = models.CharField('Privacy Level', max_length=1, choices=PRIVACY_LEVELS)
    data = JSONField('Item Data')
    created_at = models.DateTimeField('Created Date', auto_now_add=True)
    updated_at = models.DateTimeField('Updated Date', auto_now=True)
