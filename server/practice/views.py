from django.shortcuts import render

from rest_framework import viewsets,filters,permissions,generics
from .serializers import ItemSerializer
from .models import Item

# Create your views here.
# 商品一覧を表示するためのview
class ItemListView(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

# 商品詳細情報ページのためのview
class ItemDetailView(generics.RetrieveAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

 # 商品をPOSTするためのview
class ItemCreateView(generics.CreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class ItemEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    