from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.account.views import RegisterApiView, ChangePasswordApiView, \
    ForgotPasswordApiView, ForgotCompleteAPIView, ProfileAPIView, ReturnUserIdAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('profile', ProfileAPIView)
router.register('register', RegisterApiView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/', ChangePasswordApiView.as_view()),
    path('forgot_password/', ForgotPasswordApiView.as_view()),
    path('forgot_password_complete/', ForgotCompleteAPIView.as_view()),
    path('get_user_id/', ReturnUserIdAPIView.as_view())
]
