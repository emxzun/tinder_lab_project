from django.db import models
from django.contrib.auth.models import User
from applications.account.models import Profile 



class LikeDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
