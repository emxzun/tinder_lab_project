from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.likedislike.views import LikeDislikeAPIView

router = DefaultRouter()
router.register('', LikeDislikeAPIView)

urlpatterns = [
    path('', include(router.urls)),
]