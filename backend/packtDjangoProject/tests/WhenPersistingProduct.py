#! python
from decimal import Decimal
from django.test import TestCase
from packtDjangoApp.models import Product
from packtDjangoApp.models import CurrencyEnum
from .BaseUnitTest import buidProduct


class TestWhenPersistingProduct(TestCase):
    

    def testShouldCreateAnInstance(self):
        
        ''' Given: an instance '''
        product: Product = buidProduct()
        
        ''' When: saving the instance '''
        product.save()

        ''' Then: the instance is saved in the DB '''
        persistedProducts = Product.objects.all()
        self.assertEquals(persistedProducts.count(), 1)


    def testShouldReadAnInstance(self):
        
        ''' Given: a persisted instance '''
        product: Product = Product.objects.create(name="Product1", price=55.20, currency=CurrencyEnum.EUR)
        product.save()
        
        ''' When: reading the instance '''
        persidedProduct = Product.objects.get(pk=1)

        ''' Then: the instance is read from the DB'''
        self.assertIsNotNone(persidedProduct)
        self.assertEquals('Product1', persidedProduct.name)
        self.assertEquals(Decimal('55.20'), persidedProduct.price)
        self.assertEquals(CurrencyEnum.EUR, persidedProduct.currency)

    def testShouldUpdateAnInstance(self):
        
        ''' Given: a persisted instance '''
        product: Product = Product.objects.create(name="Product1", price=55.20, currency=CurrencyEnum.EUR)
        product.save()
        persidedProduct = Product.objects.get(pk=1)

        ''' When: updating the instance '''
        persidedProduct.price=25.30
        persidedProduct.save()

        ''' Then: the instance is updated in the DB'''
        updatedProduct = Product.objects.get(pk=1)
        self.assertIsNotNone(persidedProduct)
        self.assertEquals('Product1', updatedProduct.name)
        self.assertEquals(Decimal('25.30'), updatedProduct.price)
        self.assertEquals(CurrencyEnum.EUR, updatedProduct.currency)

    def testShouldDeleteAnInstance(self):
        
        ''' Given: a persisted instance '''
        product: Product = Product.objects.create(name="Product1", price=55.20, currency=CurrencyEnum.EUR)
        product.save()
        persidedProduct = Product.objects.get(pk=1)

        ''' When: deleting the instance '''
        persidedProduct.delete()

        ''' Then: the instance is deleted from the DB'''
        persistedProducts = Product.objects.all()
        self.assertEquals(persistedProducts.count(), 0)