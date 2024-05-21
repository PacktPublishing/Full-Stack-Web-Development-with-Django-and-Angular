#! python
from decimal import Decimal
from django.test import TestCase
from .BaseUnitTest import persistProduct
from packtDjangoApp.models import CurrencyEnum, Product

class TestWhenFindingProduct(TestCase):
    

    def testShouldFindAnInstanceByName(self):
        
        ''' Given: a persisted instance '''
        persistProduct()
        
        ''' When: finding the instance by Name'''
        persidedInstance = Product.objects.get(name='Product 1')

        ''' Then: the instance is read from the DB'''
        self.assertIsNotNone(persidedInstance)
        self.assertEquals('Product 1', persidedInstance.name)
        self.assertEquals(Decimal('55.20'), persidedInstance.price)
        self.assertEquals(CurrencyEnum.EUR, persidedInstance.currency)