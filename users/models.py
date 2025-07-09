from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=15, blank=False, default='')
    phone = models.CharField(max_length=15, blank=True)