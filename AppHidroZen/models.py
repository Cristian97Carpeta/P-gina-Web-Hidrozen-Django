from django.db import models

class Plantas (models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

