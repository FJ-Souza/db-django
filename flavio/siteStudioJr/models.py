from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    fone = models.IntegerField()
    data = models.CharField(max_length=10)
    tema = models.CharField(max_length=100)