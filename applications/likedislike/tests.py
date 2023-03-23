
from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse, resolve
from django.test import TestCase, SimpleTestCase

from applications.likedislike.views import SetLikeAPIView, SetDisLikeAPIView, GetLikeDislikeAPIView
from applications.account.models import Profile, User


URL_TOKEN_OBTAIN_PAIR = reverse('token_obtain_pair') 
URL_SET_LIKE = reverse('set_like', args=[1]) 
URL_SET_DISLIKE = reverse('set_dislake', args=[1]) 
URL_GET_STATUS_LIKE = reverse('get_status_like', args=[1])

class ApiCheckUrlsResolveTests(SimpleTestCase):
    def __test_check_url_resolve(self):
        url = reverse('set_like', args=[1])
        self.assertEqual(resolve(url).func.view_class, SetLikeAPIView)

        url = reverse('set_dislake', args=[1])
        self.assertEqual(resolve(url).func.view_class, SetDisLikeAPIView)

        url = reverse('get_status_like', args=[1])
        self.assertEqual(resolve(url).func.view_class, GetLikeDislikeAPIView)


class ApiSetGetLikeDislikeTest(APITestCase):
      
    def setUp(self):
        self.username = 'admin555'
        self.password = 'admin555'
        self.email = 'email@example.yu'
        self.user = User.objects.create_user(username=self.username, 
                                             password=self.password, 
                                             email=self.email,
                                             is_active=True)     
        self.profile  = Profile.objects.create(user=self.user, 
                                               age='35', 
                                               gender='M', 
                                               sexual_orientation='HE', 
                                               description='text', 
                                               status='LP', 
                                               interests='SP')
        
    def test_login_get_token(self):
        data = {'username': self.username, 'password': self.password}
        response = self.client.post(URL_TOKEN_OBTAIN_PAIR, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.token = response.data['access']
        print(f"Token:{self.token}")

        response = self.client.post(URL_SET_LIKE, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    