from rest_framework import serializers
from applications.likedislike.models import LikeDislike

class LikeDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeDislike
        fields = '__all__'