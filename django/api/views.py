from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import ItemSerializer

from items.models import Item


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer