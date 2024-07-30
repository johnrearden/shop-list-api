from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import List, ListItem, Category
from .serializers import ListSerializer, ListItemSerializer, CategorySerializer


class ListsView(ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ListDetail(RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]


class Categories(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



