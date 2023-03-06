from django.db import models

# Create your models here.
class Fracciones(models.Model):
    primerNum = models.IntegerField()
    primerDen = models.IntegerField()
    segundoNum = models.IntegerField()
    segundoDen = models.IntegerField()