#! python
from django.test import TestCase
from .TestBase import USER_NAME, persistAccount
from packtDjangoApp.models import Account, User

class TestWhenFindingAccount(TestCase):
    
    def testShouldFindAnInstanceByUsername(self):
        
        ''' Given: a persisted instance '''
        persistAccount()
        
        ''' When: finding the instance by username'''
        persidedInstance = Account.objects.get(user=User.objects.get(username=USER_NAME))

        ''' Then: the instance is read from the DB'''
        self.assertIsNotNone(persidedInstance)
        self.assertEquals('user1@packt.com', persidedInstance.user.email)
        self.assertEquals('Street 1', persidedInstance.address.street)