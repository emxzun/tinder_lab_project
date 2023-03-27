from rest_framework import serializers
from django.contrib.auth import get_user_model
from applications.notification.models import Notification
from applications.notification.tasks import send_notification_like, send_notification_chat

User = get_user_model()
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

    def create(self, validated_data):
        sender = self.context['request'].user.profile
        recipient = validated_data['recipient']
        type = validated_data['type']
        notification = Notification.objects.create(sender=sender, recipient=recipient, type=type)
        send_notification_like(recipient.user.email, notification)
        send_notification_chat(recipient.user.email, notification)
        return notification



