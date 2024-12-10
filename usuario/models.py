from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


User = get_user_model()
class extdata(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
        
                