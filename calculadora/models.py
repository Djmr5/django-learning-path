from django.db import models
from fractions import Fraction

# Create your models here.
class Fracciones(models.Model):
    primerNum = models.IntegerField()
    primerDen = models.IntegerField()
    operador = models.CharField(max_length=1)
    segundoNum = models.IntegerField()
    segundoDen = models.IntegerField()
    result = models.CharField(max_length=200)
    def __str__(self):
        return self.result