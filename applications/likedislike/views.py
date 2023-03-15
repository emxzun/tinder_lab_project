from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from applications.likedislike.models import LikeDislike
from applications.likedislike.serializers import LikeDislikeSerializer

User = get_user_model()
class LikeDislikeAPIView(APIView):
    serializer_class = LikeDislikeSerializer
    permission_classes = [IsAuthenticated]

    
    def get(self):
        user = self.request.user
        return LikeDislike.objects.filter(who_liked=user)

    
    def post(self, request):
        serializer_class = LikeDislikeSerializer(data=request.data)
        if serializer_class.is_valid:
            serializer_class.save()
            return Response(serializer_class.errors)


