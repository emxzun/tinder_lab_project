
from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse, resolve
from django.test import SimpleTestCase

from applications.likedislike.views import SetLikeAPIView, SetDisLikeAPIView, GetLikeDislikeAPIView
from applications.account.models import Profile, User


URL_TOKEN_OBTAIN_PAIR = reverse('token_obtain_pair') 
URL_SET_LIKE = reverse('set_like', args=[1]) 
URL_SET_DISLIKE = reverse('set_dislake', args=[1]) 
URL_GET_STATUS_LIKE = reverse('get_status_like', args=[1])

class ApiCheckUrlsTests(SimpleTestCase):
    '''Класс валидации маршрутов установки/получения статуса like/dislike
        тест запускается py .\manage.py test applications.likedislike.tests
    '''
    def test_check_url(self):
        '''Функция валидации маршрутов для установки и получения статуса like/dislike
        '''
        self.assertEqual(resolve(URL_SET_LIKE).func.view_class, SetLikeAPIView)
        self.assertEqual(resolve(URL_SET_DISLIKE).func.view_class, SetDisLikeAPIView)
        self.assertEqual(resolve(URL_GET_STATUS_LIKE).func.view_class, GetLikeDislikeAPIView)

class ApiSetGetLikeDislikeTest(APITestCase):
    '''Класс проверки функциональности API likedislike'''
    
    def setUp(self):
        '''Функция предустановки, служит для создания 
            экземпляров - django.test.client.Client(для отправик http-запросов),
            создает переменную 'self.user', создает виртуальные модели - Profile(models.Model) и т.п. 
        '''
        #В виртаульной БД создаем экземпляр User и Profile, 
        # под данными которого создается 'self.user' для request
        self.username = 'example_username'
        self.password = 'example_password'
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
        
    def test_set_get_like_dislike(self):
        '''Функция проверки функциональности API - 
            api/v1/likedislike/like/<int:recipient_id>/
            api/v1/likedislike/dislike/<int:recipient_id>/
            api/v1/likedislike/get_status_like/<int:recipient_id>/
        '''

        #Проходим аутентификацию и получаем Token 
        data = {'username': self.username, 'password': self.password}
        response = self.client.post(URL_TOKEN_OBTAIN_PAIR, data)
        self.token = response.data['access']
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #Ставил лайк на профил и получаем ответ об успешной обработке запроса
        response = self.client.post(URL_SET_LIKE, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.data['status'], "success")
        self.assertEqual(response.data['message'], "You liked this user")

        #Ставил дизлайк на профил и получаем ответ об успешной обработке запроса
        response = self.client.post(URL_SET_DISLIKE, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.data['status'], "success")
        self.assertEqual(response.data['message'], "You disliked this user")

        #Получаем информацию об установленных ранее Like/Dislike
        response = self.client.get(URL_GET_STATUS_LIKE, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(str(list(response.data)), "[{'is_like': False, 'is_dislike': True}]")
        

