from rest_framework import serializers

from user.serializers import UserSerializer
from .models import Item, UserItem


class ItemSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'title', 'owner', 'description', 'created', 'price', 'image']


class UserItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = UserItem
        fields = ['item', 'user']
