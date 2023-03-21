from django.urls import path

from applications.likedislike.views import SetLikeAPIView, SetDisLikeAPIView, GetLikeDislikeAPIView



urlpatterns = [
    path('like/<int:recipient_id>/', SetLikeAPIView.as_view()),
    path('dislike/<int:recipient_id>/', SetDisLikeAPIView.as_view()),
    path('get_status_like/<int:recipient_id>/', GetLikeDislikeAPIView.as_view()),
]