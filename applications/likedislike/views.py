from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework import permissions
from applications.likedislike.models import LikeDislike
from applications.likedislike.serializers import LikeDislikeSerializer

class LikeDislikeAPIView(CreateAPIView, UpdateAPIView):
    serializer_class = LikeDislikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return LikeDislike.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

