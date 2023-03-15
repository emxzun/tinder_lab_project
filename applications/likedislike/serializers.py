from rest_framework import serializers
from applications.likedislike.models import LikeDislike

class LikeDislikeSerializer(serializers.Serializer):
    who_user_liked_id = serializers.ImageField()
    whom_user_liked_id = serializers.ImageField()
    like = serializers.BooleanField()
    dislike = serializers.BooleanField()