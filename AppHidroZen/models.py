from django.contrib.auth.models import AbstractUser
from django.db import models

class User (AbstractUser):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

