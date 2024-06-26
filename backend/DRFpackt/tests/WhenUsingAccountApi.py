from django.urls import reverse
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.test import APITestCase
from packtDjangoApp.models import Address, Account
from .TestBase import USER_NAME, persistAccount, persistAddress, persistUser, populateAccounts
from .RestTestBase import getAuthorizedRestClient

class TestWhenUsingAccountApi(APITestCase):

    def setUp(self):
        self.url = reverse('account-list') # /api/v0/accounts/
        self.client = getAuthorizedRestClient(self.client)


    def testShouldCreateAnInstance(self):
        
        ''' Given: an instance '''
        accountAddress: Address = persistAddress()
        accountUser: User = persistUser(USER_NAME)
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


    def testShouldFindAllInstancesWithPagination(self):
        
        ''' Given: some persisted instances '''
        populateAccounts()
        ''' And the page number is 5 '''

        ''' When: try listing all instances by page '''
        response = self.client.get(self.url, {'page': 1}, format='json')

        ''' Then: the instances are listed with pagination '''
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.assertEqual(response.data, {'count': 6, 'next': 'http://testserver/api/v0/accounts/?page=2', 'previous': None, 'results': [{'version': 0, 'address': 1, 'user': 1}, {'version': 0, 'address': 1, 'user': 2}, {'version': 0, 'address': 1, 'user': 3}, {'version': 0, 'address': 1, 'user': 4}, {'version': 0, 'address': 1, 'user': 5}]})


    def testShouldDenyAccessWithoutToken(self):
        
        ''' Given: no access token is provided '''
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + 'invalidToken')

        ''' When: try to access the endpoint without token '''
        response = self.client.get(self.url)

        ''' Then: the Access is denied '''
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.content)


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