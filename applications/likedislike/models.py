from django.db import models
from django.contrib.auth.models import User
from applications.account.models import Profile 



class LikeDislike(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
