
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from django.urls import reverse, resolve
from django.test import TestCase, SimpleTestCase

from applications.likedislike.views import SetLikeAPIView, SetDisLikeAPIView, GetLikeDislikeAPIView
from applications.account.models import Profile, User
class ApiCheckUrlsResolveTests(SimpleTestCase):
    def test_check_url_resolve(self):
        url = reverse('set_like', args=[1])
        self.assertEqual(resolve(url).func.view_class, SetLikeAPIView)

        url = reverse('set_dislake', args=[1])
        self.assertEqual(resolve(url).func.view_class, SetDisLikeAPIView)

        url = reverse('get_status_like', args=[1])
        self.assertEqual(resolve(url).func.view_class, GetLikeDislikeAPIView)


class ApiSetGetLikeDislikeTest(APITestCase):
    url_set_like = reverse('set_like', args=[1]) 
    url_status_like = reverse('get_status_like', args=[1])  

    def setUp(self):
        self.user = User.objects.create_user(username='admin555', password='admin555', email='email@example.yu')    
        self.profile  = Profile.objects.create(user=self.user, age='35', gender='M', sexual_orientation='HE', description='text', status='LP', interests='SP')
        
        self.client = APIClient()
        
        self.token = AccessToken.for_user(user=self.profile)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        
    def test_get_custom_authenticated(self):
        
        print(f"TOKEN:{self.token}")
        response = self.client.post(self.url_set_like)
        print(f"status_code:{response.status_code}")
        
        
        


        