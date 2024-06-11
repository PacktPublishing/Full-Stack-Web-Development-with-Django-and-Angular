#! python
import django
from django.test import TestCase
from packtDjangoApp.models import Account
from .TestBase import persistAccount


class TestWhenPersistingAccount(TestCase):
    

    def testShouldCreateAnInstance(self):
        
        ''' Given: an instance '''
        instance: Account = persistAccount()

        ''' When: saving the instance '''
        instance.save()

        ''' Then: the instance is saved in the DB '''
        persistedInstances = Account.objects.all()
        self.assertEquals(persistedInstances.count(), 1)


    def testShouldReadAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistAccount()
        
        ''' When: reading the instance '''
        persidedInstance = Account.objects.get(pk=1)

        ''' Then: the instance is read from the DB'''
        self.assertIsNotNone(persidedInstance)
        self.assertIsNotNone(persidedInstance.address)
        self.assertIsNotNone(persidedInstance.user)
        self.assertEquals(0, persidedInstance.version)


    def testShouldUpdateAnInstance(self):
        
        ''' Given: a persisted instance '''
        persidedInstance = self.findInstance()

        ''' When: updating the instance '''
        persidedInstance.version=1
        persidedInstance.save()

        ''' Then: the instance is updated in the DB'''
        updatedInstance = Account.objects.get(pk=1)
        self.assertIsNotNone(updatedInstance)
        self.assertIsNotNone(updatedInstance.address)
        self.assertIsNotNone(updatedInstance.user)
        self.assertEquals(1, updatedInstance.version)

    def findInstance(self):
        persistAccount()
        return Account.objects.get(pk=1)

    
    def testShouldDeleteAnInstance(self):
        
        ''' Given: a persisted instance '''
        persidedInstance = self.findInstance()

        ''' When: deleting the instance '''
        persidedInstance.delete()

        ''' Then: the instance is deleted from the DB'''
        persistedInstances = Account.objects.all()
        self.assertEquals(persistedInstances.count(), 0)

    
    def testShouldNotCreateADuplicatedInstance(self):
        
        ''' Given: an instance '''
        persistAccount()
        
        ''' Expect: an Exception if the same instance is saved in the DB '''
        with self.assertRaises(django.db.utils.IntegrityError): 
            persistAccount()