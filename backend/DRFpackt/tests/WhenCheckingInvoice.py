#! python
from django.test import TestCase
from parameterized import parameterized
from .TestBase import persistInvoice
from packtDjangoApp.models import Invoice



class TestWhenCheckingInvoice(TestCase):
    

    def testShouldHaveAStringRepresentation(self):
        
        ''' Given: an instance '''
        instance: Invoice = persistInvoice()
        
        ''' Expect: the right String representation '''
        self.assertEquals('Invoice Number: 1 Amount: 87.0010 €', str(instance))


    def testShouldHaveAHashRepresentation(self):
        
        ''' Given: an instance '''
        instance: Invoice = persistInvoice()
        
        ''' Expect: the right Hash representation '''
        self.assertEquals(1, hash(instance)) 