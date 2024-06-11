#! python
from django.test import TestCase
from packtDjangoApp.models import User
from .TestBase import persistUser


class TestWhenCheckingUser(TestCase):
    

    def testShouldHaveAStringRepresentation(self):
        
        ''' Given: an instance '''
        instance: User = persistUser()
        
        ''' Expect: the right String representation '''
        self.assertEquals('user1Name', str(instance))


    def testShouldHaveAHashRepresentation(self):
        
        ''' Given: an instance '''
        instance: User = persistUser()
        
        ''' Expect: the right Hash representation '''
        self.assertEquals(1, hash(instance))        
