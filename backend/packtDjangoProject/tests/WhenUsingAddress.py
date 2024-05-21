#! python
import unittest
from django.test import TestCase
from parameterized import parameterized
from packtDjangoApp.models import Address
from .BaseUnitTest import ADDRESS_CITY, ADDRESS_NUMBER, ADDRESS_POSTALCODE, ADDRESS_STREET, buildAddress, persistAddress


class TestWhenUsingAddress(TestCase):
    

    def testShouldHaveAStringRepresentation(self):
        
        ''' Given: an instance '''
        instance: Address = buildAddress()
        
        ''' Expect: the right String representation '''
        self.assertEquals('Street 1 22 A0001 City 1', str(instance))


    def testShouldHaveAHashRepresentation(self):
        
        ''' Given: an instance '''
        instance: Address = persistAddress()
        
        ''' Expect: the right Hash representation '''
        self.assertEquals(1, hash(instance))        


class TestSequence(unittest.TestCase):
    @parameterized.expand([
        [buildAddress(), buildAddress(), True],
        [buildAddress(), Address.build("Street 2", ADDRESS_NUMBER, ADDRESS_CITY, ADDRESS_POSTALCODE), False],
        [buildAddress(), Address.build(ADDRESS_STREET, 33, ADDRESS_CITY, ADDRESS_POSTALCODE), False],
        [buildAddress(), Address.build(ADDRESS_STREET, ADDRESS_NUMBER, ADDRESS_CITY, 'A0002'), False],
    ])

    def testShouldCheckEquality(self, instance, anotherInstance, areEqual):
        
        ''' Expect: the instances are (not) Equal '''
        self.assertEquals(areEqual, instance == anotherInstance)