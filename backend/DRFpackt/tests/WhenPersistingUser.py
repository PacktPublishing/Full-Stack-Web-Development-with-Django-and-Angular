#! python
import django
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .TestBase import USER_EMAIL, USER_NAME, USER_PASSWORD, persistUser


class TestWhenPersistingUser(TestCase):
    

    def testShouldCreateAnInstance(self):
        
        ''' Given: an instance '''

        ''' When: saving the instance '''
        persistUser(USER_NAME)

        ''' Then: the instance is saved in the DB '''
        persistedInstances = User.objects.all()
        self.assertEquals(persistedInstances.count(), 1)


    def testShouldReadAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistUser(USER_NAME)
        
        ''' When: reading the instance '''
        persidedInstance = User.objects.get(pk=1)

        ''' Then: the instance is read from the DB '''
        self.assertIsNotNone(persidedInstance)
        self.assertEquals('user1@packt.com', persidedInstance.email)
        self.assertEquals('user1Name', persidedInstance.username)
        self.assertIsNotNone(persidedInstance.password, 'User Password')
        self.assertTrue(persidedInstance.is_active)


    def testShouldUpdateAnInstance(self):
        
        ''' Given: a persisted instance '''
        persidedInstance = self.findInstance()

        ''' When: updating the instance '''
        persidedInstance.password='NewP_ass0rd***'
        persidedInstance.save()

        ''' Then: the instance is updated in the DB '''
        updatedInstance = User.objects.get(pk=1)
        self.assertIsNotNone(updatedInstance)
        self.assertEquals('user1@packt.com', persidedInstance.email)
        self.assertEquals('user1Name', persidedInstance.username)
        self.assertEquals('NewP_ass0rd***', persidedInstance.password)
        self.assertTrue(persidedInstance.is_active)


    def findInstance(self):
        persistUser(USER_NAME)
        return User.objects.get(pk=1)

    
    def testShouldDeleteAnInstance(self):
        
        ''' Given: a persisted instance '''
        persidedInstance = self.findInstance()

        ''' When: deleting the instance '''
        persidedInstance.delete()

        ''' Then: the instance is deleted from the DB '''
        persistedInstances = User.objects.all()
        self.assertEquals(persistedInstances.count(), 0)

    
    def testShouldNotCreateADuplicatedInstance(self):
        
        ''' Given: an instance '''
        persistUser(USER_NAME)
        
        ''' Expect: an Exception if the same instance is saved in the DB '''
        with self.assertRaises(django.db.utils.IntegrityError): 
            User.objects.create(email=USER_EMAIL, password=make_password(USER_PASSWORD), username=USER_NAME, is_active=True)