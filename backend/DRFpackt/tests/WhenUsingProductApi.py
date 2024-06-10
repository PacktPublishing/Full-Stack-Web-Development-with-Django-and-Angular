from django.urls import reverse
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.test import APITestCase
from packtDjangoApp.models import CurrencyEnum, Product
from .BaseTest import buildProduct, persistProduct

class TestWhenUsingProductApi(APITestCase):

    def setUp(self):
        self.url = reverse('product-list') # /api/v0/products/

    def testShouldCreateAnInstance(self):
        
        ''' Given: an instance '''
        instance: Product = buildProduct()

        ''' When: saving the instance '''
        response = self.client.post(self.url, model_to_dict(instance), format='json')

        ''' Then: the instance is saved '''
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)


    def testShouldReadAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistProduct()
        self.url = self.url  + '1/'
        
        ''' When: reading the instance '''
        response = self.client.get(self.url)

        ''' Then: the instance is read '''
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 1, 'name': 'Product 1', 'price': '55.20', 'currency': '€'})

 
    def testShouldUpdateAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistProduct()
        self.url = self.url + '1/'

        ''' When: updating the instance '''
        updatedData = {'id': 1, 'name': 'Product 1', 'price': 25.30, 'currency': CurrencyEnum.EUR}
        response = self.client.put(self.url, updatedData, format='json')

        ''' Then: the instance is updated '''
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(self.url)
        self.assertEqual(response.data, {'id': 1, 'name': 'Product 1', 'price': '25.30', 'currency': '€'})

    def testShouldPartiallyUpdateAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistProduct()
        self.url = self.url + '1/'

        ''' When: partially updating the instance '''
        updatedData = {'price': 25.30}
        response = self.client.patch(self.url, updatedData, format='json')

        ''' Then: the instance is updated '''
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(self.url)
        self.assertEqual(response.data, {'id': 1, 'name': 'Product 1', 'price': '25.30', 'currency': '€'})

    def testShouldDeleteAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistProduct()
        self.url = self.url + '1/'

        ''' When: deleting the instance '''
        response = self.client.delete(self.url, format='json')

        ''' Then: the instance is deleted '''
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        persistedInstances = Product.objects.all()
        self.assertEquals(persistedInstances.count(), 0)