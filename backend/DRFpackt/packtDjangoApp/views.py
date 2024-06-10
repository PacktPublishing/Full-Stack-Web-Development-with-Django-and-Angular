from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer