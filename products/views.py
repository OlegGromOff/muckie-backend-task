from django.shortcuts import render

from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListView(generics.ListAPIView):
    """
    Returns 5 products.
    """
    queryset = Product.objects.all()[:5]
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve product by ID
    PUT: Update product
    DELETE: Delete product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    """
    POST: Create a new product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer