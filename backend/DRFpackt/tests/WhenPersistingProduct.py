#! python
from decimal import Decimal
import django
from django.test import TestCase
from packtDjangoApp.models import Product
from packtDjangoApp.models import CurrencyEnum
from .TestBase import buildProduct, persistProduct


class TestWhenPersistingProduct(TestCase):
    

    def testShouldCreateAnInstance(self):
        
        ''' Given: an instance '''
        instance: Product = buildProduct()

        ''' When: saving the instance '''
        instance.save()

        ''' Then: the instance is saved in the DB '''
        persistedInstances = Product.objects.all()
        self.assertEquals(persistedInstances.count(), 1)


    def testShouldReadAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistProduct()
        
        ''' When: reading the instance '''
        persidedInstance = Product.objects.get(pk=1)

        ''' Then: the instance is read from the DB'''
        self.assertIsNotNone(persidedInstance)
        self.assertEquals('Product 1', persidedInstance.name)
        self.assertEquals(Decimal('55.20'), persidedInstance.price)
        self.assertEquals(CurrencyEnum.EUR, persidedInstance.currency)


    def testShouldUpdateAnInstance(self):
        
        ''' Given: a persisted instance '''
        persidedInstance = self.findInstance()

        ''' When: updating the instance '''
        persidedInstance.price=Decimal('25.30')
        persidedInstance.save()

        ''' Then: the instance is updated in the DB'''
        updatedInstance = Product.objects.get(pk=1)
        self.assertIsNotNone(updatedInstance)
        self.assertEquals('Product 1', updatedInstance.name)
        self.assertEquals(Decimal('25.30'), updatedInstance.price)
        self.assertEquals(CurrencyEnum.EUR, updatedInstance.currency)

    def findInstance(self):
        persistProduct()
        return Product.objects.get(pk=1)

    
    def testShouldDeleteAnInstance(self):
        
        ''' Given: a persisted instance '''
        persidedInstance = self.findInstance()

        ''' When: deleting the instance '''
        persidedInstance.delete()

        ''' Then: the instance is deleted from the DB'''
        persistedInstances = Product.objects.all()
        self.assertEquals(persistedInstances.count(), 0)

    
    def testShouldNotCreateADuplicatedInstance(self):
        
        ''' Given: an instance '''
        persistProduct()
        
        ''' Expect: an Exception if the same instance is saved in the DB '''
        with self.assertRaises(django.db.utils.IntegrityError): 
            persistProduct()