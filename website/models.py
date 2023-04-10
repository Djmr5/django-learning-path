from django.db import models

# Create your models here.
class Log(models.Model):
    points = models.IntegerField(max_length=200)
    date = models.DateField('date added')

    def __str__(self):
        return f"date: {self.date}, points: {self.points}pts"
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=True)