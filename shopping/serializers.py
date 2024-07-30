from rest_framework import serializers
from .models import List, ListItem, Category


class ListItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListItem
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):

    items = ListItemSerializer(many=True)

    class Meta:
        model = List
        fields = '__all__'