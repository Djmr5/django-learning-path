from django.db import models
from hr.models import Employee

# Create your models here.
class Sale(models.Model):
    employee = models.IntegerField()
    date = models.DateField()
    total = models.IntegerField()

    class Meta:
        db_table = 'sales'