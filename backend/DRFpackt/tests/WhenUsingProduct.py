#! python
import unittest
from django.test import TestCase
from parameterized import parameterized
from packtDjangoApp.models import Product
from .BaseTest import PRODUCT_CURRENCY, PRODUCT_PRICE, buildProduct, persistProduct


class TestWhenUsingProduct(TestCase):
    

    def testShouldHaveAStringRepresentation(self):
        
        ''' Given: an instance '''
        instance: Product = buildProduct()
        
        ''' Expect: the right String representation '''
        self.assertEquals('Product 1: 55.2 EUR', str(instance))


    def testShouldHaveAHashRepresentation(self):
        
        ''' Given: an instance '''
        instance: Product = persistProduct()
        
        ''' Expect: the right Hash representation '''
        self.assertEquals(1, hash(instance))        


class TestSequence(unittest.TestCase):
    @parameterized.expand([
        [buildProduct(), buildProduct(), True],
        [buildProduct(), Product.build('Product2', PRODUCT_PRICE, PRODUCT_CURRENCY), False]
    ])

    def testShouldCheckEquality(self, instance, anotherInstance, areEqual):
        
        ''' Expect: the instances are (not) Equal '''
        self.assertEquals(areEqual, instance == anotherInstance)