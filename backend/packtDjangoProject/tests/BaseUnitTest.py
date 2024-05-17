#! python
from packtDjangoApp.models import Product
from packtDjangoApp.models import CurrencyEnum


def buidProduct():
    return Product.objects.create(name='Product1', price=55.20, currency=CurrencyEnum.EUR)
