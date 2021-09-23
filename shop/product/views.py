from django.shortcuts import render

from rest_framework import serializers, viewsets

from .models import Product

from .serializers import ProductSerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializers_class = ProductSerializer
