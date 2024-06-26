from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from packtDjangoApp.models import CurrencyEnum, Invoice, Product
from .TestBase import persistAccount, persistInvoice, persistProduct, populateInvoices
from .RestTestBase import getAuthorizedRestClient

class TestWhenUsingInvoiceApi(APITestCase):

    def setUp(self):
        self.url = reverse('invoice-list') # /api/v0/invoices/
        self.client = getAuthorizedRestClient(self.client)


    def testShouldCreateAnInstance(self):
        
        ''' Given: an instance '''
        persistProduct()
        Product.objects.create(name='Product 2', price=32.45, currency=CurrencyEnum.USD)
        persistAccount()

        ''' When: saving the instance '''
        response = self.client.post(self.url, {'invoice_number': 1, 'products': [1, 2], 'account': 1}, format='json')

        ''' Then: the instance is saved '''
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)


    def testShouldReadAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistInvoice()
        self.url = self.url  + '1/'
        
        ''' When: reading the instance '''
        response = self.client.get(self.url)

        ''' Then: the instance is read '''
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'invoice_number': 1, 'products': [1, 2], 'account': 1})

 
    def testShouldUpdateAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistInvoice()
        self.url = self.url + '1/'

        ''' When: updating the instance '''
        updatedData = {'invoice_number': 1, 'products': [2], 'account': 1}
        response = self.client.put(self.url, updatedData, format='json')

        ''' Then: the instance is updated '''
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(self.url)
        self.assertEqual(response.data, {'invoice_number': 1, 'products': [2], 'account': 1})


    def testShouldPartiallyUpdateAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistInvoice()
        self.url = self.url + '1/'

        ''' When: partially updating the instance '''
        updatedData = {'products': [2]}
        response = self.client.patch(self.url, updatedData, format='json')

        ''' Then: the instance is updated '''
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(self.url)
        self.assertEqual(response.data, {'invoice_number': 1, 'products': [2], 'account': 1})


    def testShouldDeleteAnInstance(self):
        
        ''' Given: a persisted instance '''
        persistInvoice()
        self.url = self.url + '1/'

        ''' When: deleting the instance '''
        response = self.client.delete(self.url, format='json')

        ''' Then: the instance is deleted '''
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        persistedInstances = Invoice.objects.all()
        self.assertEquals(persistedInstances.count(), 0)


    def testShouldFindAllInstancesWithPagination(self):
        
        ''' Given: some persisted instances '''
        populateInvoices()
        ''' And the page number is 5 '''

        ''' When: try listing all instances by page '''
        response = self.client.get(self.url, {'page': 1}, format='json')

        ''' Then: the instances are listed with pagination '''
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.assertEqual(response.data, {'count': 6, 'next': 'http://testserver/api/v0/invoices/?page=2', 'previous': None, 'results': [{'invoice_number': 1, 'products': [1, 2], 'account': 1}, {'invoice_number': 2, 'products': [], 'account': 1}, {'invoice_number': 3, 'products': [], 'account': 1}, {'invoice_number': 4, 'products': [], 'account': 1}, {'invoice_number': 5, 'products': [], 'account': 1}]})
    

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