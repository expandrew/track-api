from rest_framework import serializers

from django.contrib.auth.models import User

from items.models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'url', 'privacy', 'item_type', 'data')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')