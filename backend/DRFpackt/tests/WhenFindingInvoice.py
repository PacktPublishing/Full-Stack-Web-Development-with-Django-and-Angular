#! python
from decimal import Decimal
from django.test import TestCase
from .TestBase import USER_NAME, persistInvoice
from packtDjangoApp.models import Account, Invoice, User

class TestWhenFindingInvoice(TestCase):
    
    def testShouldFindAnInstanceByUsername(self):
        
        ''' Given: a persisted instance '''
        persistInvoice()
        
        ''' When: finding the instance by username'''
        persidedInstance = Invoice.objects.get(account=Account.objects.get(user=User.objects.get(username=USER_NAME)))

        ''' Then: the instance is read from the DB'''
        self.assertIsNotNone(persidedInstance)
        self.assertEquals(1, persidedInstance.invoice_number)
        self.assertEquals(Decimal('87.0010'), persidedInstance.amount)
        self.assertEquals(2, persidedInstance.products.count())
        self.assertEquals('user1@packt.com', persidedInstance.account.user.email)
        self.assertEquals('Street 1', persidedInstance.account.address.street)