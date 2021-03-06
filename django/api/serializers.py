from rest_framework import serializers

from items.models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'url', 'privacy', 'item_type', 'data')