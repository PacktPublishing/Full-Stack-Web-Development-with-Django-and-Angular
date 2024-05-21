#! python
from django.test import TestCase
from parameterized import parameterized
from .BaseUnitTest import persistAccount
from packtDjangoApp.models import Account, Account

class TestWhenUsingAccount(TestCase):
    
    def testShouldHaveAStringRepresentation(self):
        
        ''' Given: an instance '''
        instance: Account = persistAccount()
        
        ''' Expect: the right String representation '''
        self.assertEquals('user1@packt.com', str(instance))


    def testShouldHaveAHashRepresentation(self):
        
        ''' Given: an instance '''
        instance: Account = persistAccount()
        
        ''' Expect: the right Hash representation '''
        self.assertEquals(1, hash(instance))