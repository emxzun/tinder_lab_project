from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from applications.likedislike.models import LikeDislike
from applications.likedislike.serializers import LikeDislikeSerializer

class LikeDislikeAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeDislikeSerializer
    queryset = LikeDislike.objects.all()
    
    