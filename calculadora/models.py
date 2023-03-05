from django.db import models

# Create your models here.
class Fracciones(models.Model):
    primerNum = models.IntegerField(max_length=50)
    primerDen = models.IntegerField(max_length=50)
    segundoNum = models.IntegerField(max_length=50)
    segundoDen = models.IntegerField(max_length=50)