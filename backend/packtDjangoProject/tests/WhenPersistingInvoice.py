#! python
from decimal import Decimal
import django
from django.test import TestCase
from packtDjangoApp.models import Account, Invoice, Product
from .BaseTest import PRODUCT_CURRENCY, PRODUCT_PRICE, persistInvoice


class TestWhenPersistingInvoice(TestCase):
    

    def testShouldCreateAnInstance(self):
        
        ''' Given: an instance '''

        ''' When: saving the instance '''
        persistInvoice()

        ''' Then: the instance is saved in the DB '''
        persistedInstances = Invoice.objects.all()
        self.assertEquals(persistedInstances.count(), 1)


    def testShouldReadAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistInvoice()
        
        ''' When: reading the instance '''
        persidedInstance = Invoice.objects.get(pk=1)

        ''' Then: the instance is read from the DB'''
        self.assertIsNotNone(persidedInstance)
        self.assertEquals(1, persidedInstance.invoice_number)
        self.assertEquals(Decimal('87.0010'), persidedInstance.amount)
        self.assertEquals(2, persidedInstance.products.count())
        self.assertIsNotNone(persidedInstance.account)


    def testShouldUpdateAnInstance(self):
        
        ''' Given: a persisted instance '''
        persidedInstance = self.findInstance()

        ''' When: updating the instance '''
        persidedInstance.invoice_number=2
        product: Product = Product.objects.create(name='Product 3', price=PRODUCT_PRICE, currency=PRODUCT_CURRENCY)
        persidedInstance.products.add(product)
        persidedInstance.save()

        ''' Then: the instance is updated in the DB'''
        updatedInstance = Invoice.objects.get(pk=1)
        self.assertIsNotNone(updatedInstance)
        self.assertEquals(2, updatedInstance.invoice_number)
        self.assertEquals(Decimal('142.2010'), updatedInstance.amount)
        self.assertEquals(3, updatedInstance.products.count())
        self.assertIsNotNone(persidedInstance.account)

    def findInstance(self):
        persistInvoice()
        persidedInstance = Invoice.objects.get(pk=1)
        return persidedInstance

    
    def testShouldDeleteAnInstance(self):
        
        ''' Given: a persisted instance '''
        persidedInstance = self.findInstance()

        ''' When: deleting the instance '''
        persidedInstance.delete()

        ''' Then: the instance is deleted from the DB'''
        persistedInstances = Invoice.objects.all()
        self.assertEquals(persistedInstances.count(), 0)
        ''' And: the Product instances are kept in the DB'''
        persistedProducts = Product.objects.all()
        self.assertEquals(persistedProducts.count(), 2)
        ''' And: the Account instance is kept in the DB'''
        self.assertEquals(Account.objects.all().count(), 1)