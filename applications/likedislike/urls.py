from django.urls import path

from applications.likedislike.views import LikeCreateAPIView, SetDislikeAPIView, GetStatusLikeAPIView



urlpatterns = [
    path('like/', LikeCreateAPIView.as_view(), name='like'),
    path('dislike/', SetDislikeAPIView.as_view(), name='dislike'),
    path('status_like/', GetStatusLikeAPIView.as_view(), name='get_status_like'),
]
