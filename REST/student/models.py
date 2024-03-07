from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=40)