from rest_framework import serializers
from applications.account.models import Profile

class RecommendationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
    