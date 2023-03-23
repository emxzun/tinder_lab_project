
from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse, resolve
from django.test import SimpleTestCase

from applications.recommendations.views import RecommendationsApiView
from applications.account.models import Profile, User


URL_TOKEN_OBTAIN_PAIR = reverse('token_obtain_pair') 
URL_RECOMMENDATIONS = reverse('recommendations') 

class ApiCheckUrlsTests(SimpleTestCase):
    '''Класс валидации маршрута по 'recommendations'
        тест запускается py .\manage.py test applications.recommendations.tests
    '''
    def test_check_url(self):
        '''Функция валидации маршрута по 'recommendations'
        '''
        self.assertEqual(resolve(URL_RECOMMENDATIONS).func.view_class, RecommendationsApiView)

class ApiRecommendationsTest(APITestCase):
    '''Класс проверки функциональности API recommendations'''
    
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
        #Также создаются еще два Profile у которых одинаковые значения
        # по фильтрам - Интересы, Статус, Ориентация, Возраст
        self.username_2 = 'example_username_2'
        self.password_2 = 'example_password_2'
        self.email_2 = 'email@example_2.yu'
        self.user_2 = User.objects.create_user(username=self.username_2, 
                                             password=self.password_2, 
                                             email=self.email_2,
                                             is_active=True)     
        self.profile_2  = Profile.objects.create(user=self.user_2, 
                                               age='35', 
                                               gender='M', 
                                               sexual_orientation='HE', 
                                               description='text', 
                                               status='LP', 
                                               interests='SP')
        
        self.username_3 = 'example_username_3'
        self.password_3 = 'example_password_3'
        self.email_3 = 'email@example_3.yu'
        self.user_3 = User.objects.create_user(username=self.username_3, 
                                             password=self.password_3, 
                                             email=self.email_3,
                                             is_active=True)     
        self.profile_3  = Profile.objects.create(user=self.user_3, 
                                               age='35', 
                                               gender='M', 
                                               sexual_orientation='HE', 
                                               description='text', 
                                               status='LP', 
                                               interests='SP')

        
    def test_recommendations(self):
        '''Функция проверки функциональности API - 
            api/v1/recommendations/
        '''

        #Проходим аутентификацию и получаем Token 
        data = {'username': self.username, 'password': self.password}
        response = self.client.post(URL_TOKEN_OBTAIN_PAIR, data)
        self.token = response.data['access']
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #Получаем список Profile'ей рекомендованных self.profile, который 
        # осуществляет запрос
        response = self.client.get(URL_RECOMMENDATIONS, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        data = response.data

        #Сравнение self.profile(user-который осуществялет запрос) с 
        # self.profile_1 по Интересам, Статусу, Ориентации, Возрасту
        self.assertEqual(self.profile.interests, data[0]['interests'])
        self.assertEqual(self.profile.status, data[0]['status'])
        self.assertEqual(self.profile.sexual_orientation, data[0]['sexual_orientation'])
        self.assertEqual(self.profile.age, data[0]['age'])

        #Сравнение self.profile(user-который осуществялет запрос) с 
        # self.profile_2 по Интересам, Статусу, Ориентации, Возрасту
        self.assertEqual(self.profile.interests, data[1]['interests'])
        self.assertEqual(self.profile.status, data[1]['status'])
        self.assertEqual(self.profile.sexual_orientation, data[1]['sexual_orientation'])
        self.assertEqual(self.profile.age, data[1]['age'])
      
