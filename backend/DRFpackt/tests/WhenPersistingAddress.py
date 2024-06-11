#! python
from django.test import TestCase
from packtDjangoApp.models import Address
from .TestBase import buildAddress, persistAddress

class TestWhenPersistingAddress(TestCase):
    

    def testShouldCreateAnInstance(self):
        
        ''' Given: an instance '''
        instance: Address = buildAddress()
        
        ''' When: saving the instance '''
        instance.save()

        ''' Then: the instance is saved in the DB '''
        persistedInstances = Address.objects.all()
        self.assertEquals(persistedInstances.count(), 1)


    def testShouldReadAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistAddress()
        
        ''' When: reading the instance '''
        persidedInstance = Address.objects.get(pk=1)

        ''' Then: the instance is read from the DB'''
        self.assertIsNotNone(persidedInstance)
        self.assertEquals('Street 1', persidedInstance.street)
        self.assertEquals(22, persidedInstance.number)
        self.assertEquals('City 1', persidedInstance.city)
        self.assertEquals('A0001', persidedInstance.postal_code)

    
    def testShouldUpdateAnInstance(self):
        
        ''' Given: a persisted instance '''
        persidedInstance = self.findInstance()

        ''' When: updating the instance '''
        persidedInstance.number=33
        persidedInstance.save()

        ''' Then: the instance is updated in the DB'''
        updatedInstance = Address.objects.get(pk=1)
        self.assertIsNotNone(updatedInstance)
        self.assertEquals('Street 1', updatedInstance.street)
        self.assertEquals(33, updatedInstance.number)
        self.assertEquals('City 1', updatedInstance.city)
        self.assertEquals('A0001', updatedInstance.postal_code)
    
    def findInstance(self):
        persistAddress()
        persidedInstance = Address.objects.get(pk=1)
        return persidedInstance

    
    def testShouldDeleteAnInstance(self):
        
        ''' Given: a persisted instance '''
        persidedInstance = self.findInstance()

        ''' When: deleting the instance '''
        persidedInstance.delete()

        ''' Then: the instance is deleted from the DB'''
        persidedInstances = Address.objects.all()
        self.assertEquals(persidedInstances.count(), 0)