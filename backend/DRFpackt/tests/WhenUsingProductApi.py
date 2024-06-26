from django.urls import reverse
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.test import APITestCase
from packtDjangoApp.models import CurrencyEnum, Product
from .TestBase import buildProduct, persistProduct, populateProducts
from .RestTestBase import getAuthorizedRestClient

class TestWhenUsingProductApi(APITestCase):

    def setUp(self):
        self.url = reverse('product-list') # /api/v0/products/
        self.client = getAuthorizedRestClient(self.client)

    def testShouldCreateAnInstance(self):
        
        ''' Given: an instance '''
        instance: Product = buildProduct()
        ''' And: an authenticated user'''


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


    def testShouldFindAllInstancesWithPagination(self):
        
        ''' Given: some persisted instances '''
        populateProducts()
        ''' And the page number is 5 '''

        ''' When: try listing all instances by page '''
        response = self.client.get(self.url, {'page': 1}, format='json')

        ''' Then: the instances are listed with pagination '''
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.assertEqual(response.data, {'count': 6, 'next': 'http://testserver/api/v0/products/?page=2', 'previous': None, 'results': [{'id': 1, 'name': 'Product 1', 'price': '55.20', 'currency': '€'}, {'id': 2, 'name': 'Product 2', 'price': '55.20', 'currency': '€'}, {'id': 3, 'name': 'Product 3', 'price': '55.20', 'currency': '€'}, {'id': 4, 'name': 'Product 4', 'price': '55.20', 'currency': '€'}, {'id': 5, 'name': 'Product 5', 'price': '55.20', 'currency': '€'}]})


    def testShouldDenyAccessWithoutToken(self):
        
        ''' Given: no access token is provided '''
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + 'invalidToken')
        ''' And: a secured REST Endpoint from the API '''

        ''' When: try to access the endpoint without token '''
        response = self.client.get(self.url)

        ''' Then: the Access is denied '''
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.content)


    def testShouldAllowAccessWithToken(self):
        
        ''' Given: a user access Token '''
        self.client = getAuthorizedRestClient(self.client)
        ''' And: a secured REST Endpoint from the API '''

        ''' When: try to access the endpoint with token '''
        response = self.client.get(self.url)

        ''' Then: the Access is allowed '''
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)