from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    account = models.TextField(default='')
    name = models.TextField(default='')
