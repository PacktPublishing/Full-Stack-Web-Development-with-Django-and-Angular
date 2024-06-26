from django.urls import reverse
from django.contrib.auth.models import User
from .TestBase import USER_NAME, USER_PASSWORD, persistUser

def getAccessToken(client):
    try:
        User.objects.get(username=USER_NAME)
    except:
        persistUser(USER_NAME)
    accesTokenEndpoint = reverse('token_obtain_pair') # /api/token/
    response = client.post(accesTokenEndpoint, {'username': USER_NAME, 'password': USER_PASSWORD}, format='json')
    accessToken = response.data['access']
    return accessToken

def getAuthorizedRestClient(client):
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + getAccessToken(client))
    return client
