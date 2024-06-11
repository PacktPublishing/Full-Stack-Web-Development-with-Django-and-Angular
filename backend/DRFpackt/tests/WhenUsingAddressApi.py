from django.urls import reverse
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.test import APITestCase
from packtDjangoApp.models import Address
from .TestBase import buildAddress, persistAddress

class TestWhenUsingAddressApi(APITestCase):

    def setUp(self):
        self.url = reverse('address-list') # /api/v0/addresses/

    def testShouldCreateAnInstance(self):
        
        ''' Given: an instance '''
        instance: Address = buildAddress()

        ''' When: saving the instance '''
        response = self.client.post(self.url, model_to_dict(instance), format='json')

        ''' Then: the instance is saved '''
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Address.objects.count(), 1)


    def testShouldReadAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistAddress()
        self.url = self.url  + '1/'
        
        ''' When: reading the instance '''
        response = self.client.get(self.url)

        ''' Then: the instance is read '''
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 1, 'street': 'Street 1', 'number': 22, 'city': 'City 1', 'postal_code': 'A0001'})

 
    def testShouldUpdateAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistAddress()
        self.url = self.url + '1/'

        ''' When: updating the instance '''
        updatedData = {'id': 1, 'street': 'Street 1', 'number': 33, 'city': 'City 1', 'postal_code': 'A0001'}
        response = self.client.put(self.url, updatedData, format='json')

        ''' Then: the instance is updated '''
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(self.url)
        self.assertEqual(response.data, {'id': 1, 'street': 'Street 1', 'number': 33, 'city': 'City 1', 'postal_code': 'A0001'})

    def testShouldPartiallyUpdateAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistAddress()
        self.url = self.url + '1/'

        ''' When: partially updating the instance '''
        updatedData = {'number': 33}
        response = self.client.patch(self.url, updatedData, format='json')

        ''' Then: the instance is updated '''
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(self.url)
        self.assertEqual(response.data, {'id': 1, 'street': 'Street 1', 'number': 33, 'city': 'City 1', 'postal_code': 'A0001'})

    def testShouldDeleteAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistAddress()
        self.url = self.url + '1/'

        ''' When: deleting the instance '''
        response = self.client.delete(self.url, format='json')

        ''' Then: the instance is deleted '''
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        persistedInstances = Address.objects.all()
        self.assertEquals(persistedInstances.count(), 0)