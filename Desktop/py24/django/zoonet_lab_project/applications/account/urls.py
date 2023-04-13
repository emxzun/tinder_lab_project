from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.account.views import RegisterApiView, ChangePasswordApiView,ForgotPasswordApiView, ForgotCompleteAPIView, ProfileAPIView, ActivationApiView, SendSMSAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('profile', ProfileAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterApiView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationApiView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/', ChangePasswordApiView.as_view()),
    path('forgot_password/', ForgotPasswordApiView.as_view()),
    path('forgot_password_complete/', ForgotCompleteAPIView.as_view()),
    path('send_sms/', SendSMSAPIView.as_view()),
]
