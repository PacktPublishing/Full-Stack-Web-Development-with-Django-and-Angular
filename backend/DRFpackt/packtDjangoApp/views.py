from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Product, Address, Account, Invoice
from .serializers import ProductSerializer, AddressSerializer, AccountSerializer, InvoiceSerializer

# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows addresses to be viewed or edited.
    """
    queryset = Address.objects.all().order_by('postal_code')
    serializer_class = AddressSerializer

class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """
    queryset = Account.objects.all().order_by('user')
    serializer_class = AccountSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows invoices to be viewed or edited.
    """
    queryset = Invoice.objects.all().order_by('account')
    serializer_class = InvoiceSerializer