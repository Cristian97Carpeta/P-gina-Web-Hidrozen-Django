from django.contrib.auth.models import AbstractUser
from django.db import models

class User (AbstractUser):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
class Planta(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    necesita_riego = models.BooleanField(default=False)
    riego_automatico = models.BooleanField(default=True)
