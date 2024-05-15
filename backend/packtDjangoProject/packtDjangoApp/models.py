from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class Address(models.Model):
    
    street = models.CharField(max_length=254)
    number = models.IntegerField(null=True)
    city = models.CharField(max_length=150)
    postal_code = models.CharField("postalCode", max_length=150)

    class Meta:
        ordering = ['postal_code']

    def __str__(self):
        return f"{self.street} {self.number} {self.postal_code} {self.city}"
    

class CurrencyEnum(models.TextChoices):

    EUR = '€'
    USD = '$'

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField("productName", max_length=200) 
    price = models.DecimalField(max_digits=10, decimal_places=2, default=00)
    currency = models.CharField(
        max_length=3,
        choices=CurrencyEnum,
        default=CurrencyEnum.EUR
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}: {self.price} {self.currency}"
    
class Invoice(models.Model):

    invoice_number = models.IntegerField(default=0)
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ['invoice_number']

    def calculateAmount(self):
        totalAmount = 0
        for product in self.products.all():
            if product.currency == CurrencyEnum.EUR:
                totalAmount += product.price * Decimal('1.00')
            if product.currency == CurrencyEnum.USD: totalAmount += product.price * Decimal('0.98')  
            else: totalAmount += 0
        return totalAmount
    
    amount = property(calculateAmount)

    def __str__(self):
        return f"Invoice Number: {self.invoice_number} Amount: {self.amount} €"


class Account(models.Model):

    creation_date = models.DateTimeField("creationDate")
    last_update = models.DateTimeField("lastUpdate")
    enabled = models.BooleanField
    version = models.IntegerField(default=0)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, null=False, blank=False)
    invoices = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user.email