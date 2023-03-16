from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationAPIView

router = DefaultRouter()
router.register('notification', NotificationAPIView)


urlpatterns = [

    path('', include(router.urls)),

]
