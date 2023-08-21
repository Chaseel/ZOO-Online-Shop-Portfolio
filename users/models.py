from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', null=True, blank=True)
    about_us = models.CharField(default='',max_length=1024)