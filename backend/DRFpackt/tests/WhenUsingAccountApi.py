from django.urls import reverse
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.test import APITestCase
from packtDjangoApp.models import Address, Account
from .TestBase import persistAddress, persistUser, persistAccount

class TestWhenUsingAccountApi(APITestCase):

    def setUp(self):
        self.url = reverse('account-list') # /api/v0/accounts/

    def testShouldCreateAnInstance(self):
        
        ''' Given: an instance '''
        accountAddress: Address = persistAddress()
        accountUser: User = persistUser()
        instance: Account = Account.build(accountAddress, accountUser)

        ''' When: saving the instance '''
        response = self.client.post(self.url, model_to_dict(instance), format='json')

        ''' Then: the instance is saved '''
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)


    def testShouldReadAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistAccount()
        self.url = self.url  + '1/'
        
        ''' When: reading the instance '''
        response = self.client.get(self.url)

        ''' Then: the instance is read '''
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'version': 0, 'address': 1, 'user': 1})

 
    def testShouldUpdateAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistAccount()
        self.url = self.url + '1/'

        ''' When: updating the instance '''
        updatedData = {'version': 1, 'address': 1, 'user': 1}
        response = self.client.put(self.url, updatedData, format='json')

        ''' Then: the instance is updated '''
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(self.url)
        self.assertEqual(response.data, {'version': 1, 'address': 1, 'user': 1})

    def testShouldPartiallyUpdateAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistAccount()
        self.url = self.url + '1/'

        ''' When: partially updating the instance '''
        updatedData = {'version': 1}
        response = self.client.patch(self.url, updatedData, format='json')

        ''' Then: the instance is updated '''
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(self.url)
        self.assertEqual(response.data, {'version': 1, 'address': 1, 'user': 1})

    def testShouldDeleteAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistAccount()
        self.url = self.url + '1/'

        ''' When: deleting the instance '''
        response = self.client.delete(self.url, format='json')

        ''' Then: the instance is deleted '''
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        persistedInstances = Account.objects.all()
        self.assertEquals(persistedInstances.count(), 0)