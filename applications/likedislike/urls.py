from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.likedislike.views import LikeDislikeAPIView


urlpatterns = [
    path('', LikeDislikeAPIView.as_view()),

]
