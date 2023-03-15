from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class LikeDislike(models.Model):
    who_user_liked_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='who_likedislike', verbose_name="Кто поставил лайк/дизлайк")
    whom_user_liked_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='whom_likedislike', verbose_name="На кого поставили лайк/дизлайк")
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Лайк-Дизлайк'
        verbose_name_plural = 'Лайки-Дизлайки'
