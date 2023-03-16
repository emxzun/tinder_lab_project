from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from applications.likedislike.models import LikeDislike
from applications.likedislike.serializers import LikeDislikeSerializer

class LikeDislikeAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LikeDislikeSerializer
    
    def post(self, request, who_user_liked_id):
        serializer_class = LikeDislikeSerializer(data=request.data)
        if serializer_class.is_valid:
            data = serializer_class.validated_data
            like = data.get('like')
            dislike = data.get('dislike')
            LikeDislike.objects.update_or_create(who_user_liked_id=request.user,
                                                 whom_user_liked_id=who_user_liked_id,
                                                 like=like,
                                                 dislike=dislike)
        return Response("success")
    
    def get(self, request, whom_user_liked_id):
        obj_likes = LikeDislike.objects.get(who_user_liked_id=request.user,
                                            whom_user_liked_id=whom_user_liked_id)
        serialize = LikeDislikeSerializer(instance=obj_likes, many=True)
        return Response(serialize.data)




    
    