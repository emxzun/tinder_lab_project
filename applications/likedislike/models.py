from django.db import models
from applications.account.models import Profile

class LikeDislike(models.Model):
    who_profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, 
                                          related_name='wholikedislake', 
                                          verbose_name="profile_id - Кто поставил лайк/дизлайк")
    whom_profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, 
                                           related_name='whomlikedislake', 
                                           verbose_name="profile_id - На кого поставили лайк/дизлайк")
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

    def __str__(self):
        return self.who_user_liked_id
    class Meta:
        verbose_name = 'Лайк-Дизлайк'
        verbose_name_plural = 'Лайки-Дизлайки'
