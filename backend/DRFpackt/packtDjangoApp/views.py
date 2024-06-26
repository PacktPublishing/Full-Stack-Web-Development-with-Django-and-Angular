from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product, Address, Account, Invoice
from .serializers import ProductSerializer, AddressSerializer, AccountSerializer, InvoiceSerializer

# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows addresses to be viewed or edited.
    """
    queryset = Address.objects.all().order_by('postal_code')
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """
    queryset = Account.objects.all().order_by('user')
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows invoices to be viewed or edited.
    """
    queryset = Invoice.objects.all().order_by('account')
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]    