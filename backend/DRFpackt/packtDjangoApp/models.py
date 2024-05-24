from datetime import datetime
import django
from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class Address(models.Model):
    
    street = models.CharField(max_length=254)
    number = models.IntegerField(null=True)
    city = models.CharField(max_length=150)
    postal_code = models.CharField("postalCode", max_length=150)

    @classmethod
    def build(cls, addressStreet, addressNumber, addressCity, addressPostalcode):
        instance = cls(street=addressStreet, number=addressNumber, city=addressCity, postal_code=addressPostalcode)
        return instance

    class Meta:
        ordering = ['postal_code']

    def __str__(self):
        return f"{self.street} {self.number} {self.postal_code} {self.city}"
    
    def __eq__(self, other):
        return (
            isinstance(other, Address) and
            self.street == other.street and self.number == other.number and self.postal_code == other.postal_code
        )
    
    def __hash__(self):
        return self.pk
    

class CurrencyEnum(models.TextChoices):

    EUR = '€'
    USD = '$'

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField("productName", max_length=200, unique=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2, default=00)
    currency = models.CharField(
        max_length=3,
        choices=CurrencyEnum,
        default=CurrencyEnum.EUR
    )

    @classmethod
    def build(cls, productName, productPrice, productCurrency):
        instance = cls(name=productName, price=productPrice, currency=productCurrency)
        return instance

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name}: {self.price} {self.currency}"
    
    def __eq__(self, other):
        return (
            isinstance(other, Product) and
            self.name == other.name
        )
    
    def __hash__(self):
        return self.pk


class Account(models.Model):

    creation_date = models.DateTimeField("creationDate", auto_now=True)
    last_update = models.DateTimeField("lastUpdate", auto_now=True)
    enabled = models.BooleanField
    version = models.IntegerField(default=0)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['user']

    @classmethod
    def build(cls, accountAddress, accountUser):
        instance = cls(address=accountAddress, user=accountUser)
        return instance

    def __str__(self):
        return self.user.email
    
    def __eq__(self, other):
        return (
            isinstance(other, Account) and
            self.user == other.user
        )
    
    def __hash__(self):
        return self.pk
    
class Invoice(models.Model):

    invoice_number = models.IntegerField(default=0)
    products = models.ManyToManyField(Product)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def calculateAmount(self):
        totalAmount = 0
        for product in self.products.all():
            if product.currency == CurrencyEnum.EUR:
                totalAmount += product.price * Decimal('1.00')
            if product.currency == CurrencyEnum.USD: totalAmount += product.price * Decimal('0.98')  
            else: totalAmount += 0
        return totalAmount
    
    amount = property(calculateAmount)

    class Meta:
        ordering = ['invoice_number']

    @classmethod
    def build(cls, invoiceNumber):
        instance = cls(invoice_number=invoiceNumber)
        return instance

    def __str__(self):
        return f"Invoice Number: {self.invoice_number} Amount: {self.amount} €"
    
    def __eq__(self, other):
        return (
            isinstance(other, Invoice) and
            self.invoice_number == other.invoice_number
        )
    
    def __hash__(self):
        return self.pk