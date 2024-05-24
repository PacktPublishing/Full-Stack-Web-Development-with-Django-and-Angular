#! python
from django.test import TestCase
from .BaseTest import USER_EMAIL, USER_NAME, persistUser
from packtDjangoApp.models import User

class TestWhenFindingUser(TestCase):
    
    def testShouldFindAnInstanceByUsername(self):
        
        ''' Given: a persisted instance '''
        persistUser()
        
        ''' When: finding the instance by username'''
        persidedInstance = User.objects.get(username=USER_NAME)

        ''' Then: the instance is read from the DB'''
        self.assertIsNotNone(persidedInstance)
        self.assertEquals('user1@packt.com', persidedInstance.email)
        self.assertEquals('user1Name', persidedInstance.username)
        self.assertEquals('P_assw0rd***', persidedInstance.password)

    def testShouldFindAnInstanceByEmail(self):
        
        ''' Given: a persisted instance '''
        persistUser()
        
        ''' When: finding the instance by email'''
        persidedInstance = User.objects.get(email=USER_EMAIL)

        ''' Then: the instance is read from the DB'''
        self.assertIsNotNone(persidedInstance)
        self.assertEquals('user1@packt.com', persidedInstance.email)
        self.assertEquals('user1Name', persidedInstance.username)
        self.assertEquals('P_assw0rd***', persidedInstance.password)