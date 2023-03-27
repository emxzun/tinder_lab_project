from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

from applications.account.models import Profile
from applications.chat.models import Chat, Message

User = get_user_model()

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    liked_profiles = models.ManyToManyField(to='self', blank=True, symmetrical=False)

    def __str__(self):
        return self.user

class Notification(models.Model):
    class Type(models.TextChoices):
        LIKE = 'LIKE', _('like')
        CHAT_REQUEST = 'CHAT_REQUEST', _('chat request')

    sender = models.ForeignKey(to=Profile, on_delete=models.CASCADE, related_name="sent_notifications")
    recipient = models.ForeignKey(to=Profile, on_delete=models.CASCADE, related_name="received_notifications")
    type = models.CharField(max_length=20, choices=Type.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'notification{self.pk}'

    def like_profile(self, profile_id):
        sender = self.sender
        recipient = Profile.objects.get(pk=profile_id)
        sender.liked_profiles.add(recipient)
        notification = Notification.objects.create(sender=sender, recepient=recipient, type=Notification.Type.LIKE)
        notification.save()
        return notification


    def send_chat_request(request, profile_id):
        sender = request.user.profile
        recepient = Profile.objects.get(pk=profile_id)
        chat = Chat.objects.create()
        chat.users.add(recepient)
        chat.users.add(sender)
        message = Message.objects.create(chat=chat, type=Message.Type.TEXT, text='i would like to chat with you!')
        notification = Notification.objects.create(sender=sender, recepient=recepient, type=Notification.Type.CHAT_REQUEST)
        notification.save()
        return redirect('profile_detail', profile_id=profile_id)


