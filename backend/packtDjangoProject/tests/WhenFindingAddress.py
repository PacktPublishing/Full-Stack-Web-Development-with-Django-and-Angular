#! python
from django.test import TestCase
from .BaseUnitTest import persistAddress
from packtDjangoApp.models import Address

class TestWhenFindingAddress(TestCase):
    

    def testShouldFindAnInstanceByStreetAndNumberAndPostalCode(self):
        
        ''' Given: a persisted instance '''
        persistAddress()
        
        ''' When: finding the instance by Street and Number and PostalCode'''
        persidedInstance = Address.objects.get(street='Street 1', number=22, postal_code='A0001')

        ''' Then: the instance is read from the DB'''
        self.assertIsNotNone(persidedInstance)
        self.assertEquals('Street 1', persidedInstance.street)
        self.assertEquals(22, persidedInstance.number)
        self.assertEquals('City 1', persidedInstance.city)
        self.assertEquals('A0001', persidedInstance.postal_code)