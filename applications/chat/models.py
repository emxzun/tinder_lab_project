from django.db import models
from django.utils.translation import gettext_lazy as _
<<<<<<< HEAD
from django.contrib.auth import get_user_model


User = get_user_model()

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE, default=True)
    content = models.TextField(default='')
    image = models.ImageField(upload_to='chat_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    block_users = models.ManyToManyField(User, related_name='blocked_chats', default=set)

    class Meta:
        ordering = ('updated_at',)








=======

from applications.account.models import Profile


class Chat(models.Model):
    class Status(models.TextChoices):
        CLOSE = 'CLOSE', _('close')
        OPEN = 'OPEN', _('open')
        BAD = 'BAN', _('ban')

    users = models.ManyToManyField(to=Profile, related_name="chats")
    ban_user = models.ForeignKey(to=Profile, on_delete=models.CASCADE, related_name="chats_with_ban")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.CLOSE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"chat_{self.pk}"


class Message(models.Model):
    class Type(models.TextChoices):
        TEXT = 'TEXT', _('text')
        IMAGE = 'IMAGE', _('image')

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=Type.choices)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="chat/images", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"message_{self.pk}"
>>>>>>> origin/mika
