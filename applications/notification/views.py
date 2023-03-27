from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from applications.notification.models import Notification
from applications.notification.serializers import NotificationSerializer

User = get_user_model()

class NotificationAPIView(ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def notifications(self, request):
        profile = request.user.profile
        notifications = profile.received_notifications.all().order_by('-created_at')
        return Response({'notifications': notifications}, status=200)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

