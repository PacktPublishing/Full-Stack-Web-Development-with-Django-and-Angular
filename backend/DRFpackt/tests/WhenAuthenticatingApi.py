from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .TestBase import USER_NAME,USER_PASSWORD, persistUser
from .RestTestBase import getAuthorizedRestClient

class TestWhenAuthenticatingApi(APITestCase):

    def setUp(self):
        persistUser(USER_NAME)
        self.accesTokenEndpoint = reverse('token_obtain_pair') # /api/token/


    def testShouldGetAccessToken(self):
        
        ''' Given: a registered user '''
        data = {'username': USER_NAME, 'password': USER_PASSWORD}
        ''' And: a REST Endpoint for getting an JWT Access Token'''
        url = reverse('token_obtain_pair') # /api/token/

        ''' When: get the JWT Access Token '''
        # curl -X POST -H "Content-Type: application/json" -d '{"username": "user", "password": "P_assw0rd***"}' http://localhost:8000/api/token/
        response = self.client.post(url, data, format='json')

        ''' Then: the Access Token is returned '''
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)
        accessToken = response.data['access']
        refreshToken = response.data['refresh']
        self.assertIsNotNone(accessToken)
        self.assertIsNotNone(refreshToken)
        print('Shortlived Access token: ' + accessToken)
        print('Longlived Refresh token: ' + refreshToken)


    def testShouldRefreshToken(self):
        
        ''' Given: a registered user '''
        response = self.client.post(self.accesTokenEndpoint, {'username': USER_NAME, 'password': USER_PASSWORD}, format='json')
        refreshToken = response.data['refresh']
        data = {'refresh': refreshToken}
        ''' And: a REST Endpoint for getting an new JWT Access Token '''
        url = reverse('token_refresh') # /api/token/refresh/

        ''' When: refresh the JWT Token after Access Token has expired '''
        # curl -X POST -H "Content-Type: application/json" -d '{"refresh": "refreshToken"}' http://localhost:8000/api/token/refresh/
        response = self.client.post(url, data, format='json')

        ''' Then: the new Access Token is returned '''
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.assertTrue('access' in response.data)
        accessToken = response.data['access']
        self.assertIsNotNone(accessToken)


    def testShouldVerifyToken(self):
        
        ''' Given: a registered user '''
        response = self.client.post(self.accesTokenEndpoint, {'username': USER_NAME, 'password': USER_PASSWORD}, format='json')
        accessToken = response.data['access']
        data = {'token': accessToken}
        ''' And: a REST Endpoint for validating a JWT Access Token '''
        url = reverse('token_verify') # /api/token/verify/

        ''' When: validate the JWT Token '''
        # curl -X POST -H "Content-Type: application/json" -d '{"token": "accessToken"}' http://localhost:8000/api/token/verify/
        response = self.client.post(url, data, format='json')

        ''' Then: the Access Token is validated '''
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)


    def testShouldDenyAccessWithoutToken(self):
        
        ''' Given: no access token '''
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + 'invalidToken')
        ''' And: a secured REST Endpoint from the API '''
        url = reverse('product-list')

        ''' When: try to access the endpoint without token '''
        # curl -X GET -H "Authorization: Bearer invalidToken" http://localhost:8000/api/v0/products/
        # curl -X GET http://localhost:8000/api/v0/products/
        response = self.client.get(url)

        ''' Then: the Access is denied '''
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.content)


    def testShouldAllowAccessWithToken(self):
        
        ''' Given: a valid user access Token '''
        self.client = getAuthorizedRestClient(self.client)
        ''' And: a secured REST Endpoint from the API '''
        url = reverse('product-list')

        ''' When: try to access the endpoint with token '''
        # curl -X GET -H "Authorization: Bearer validToken" http://localhost:8000/api/v0/products/
        response = self.client.get(url)

        ''' Then: the Access is allowed '''
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
