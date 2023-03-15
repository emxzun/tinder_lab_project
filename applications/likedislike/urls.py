from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.likes.views import LikesApiView


urlpatterns = [
    path('', LikesApiView.as_view()),

]
