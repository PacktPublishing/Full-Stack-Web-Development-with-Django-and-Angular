from django.urls import reverse
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.test import APITestCase
from packtDjangoApp.models import CurrencyEnum, Invoice, Account, Product
from .TestBase import persistAccount, persistInvoice, persistProduct

class TestWhenUsingInvoiceApi(APITestCase):

    def setUp(self):
        self.url = reverse('invoice-list') # /api/v0/invoices/

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