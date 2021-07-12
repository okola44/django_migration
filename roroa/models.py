from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    second_name=models.CharField(max_length=13)
    age=models.PositiveSmallIntegerField(max_length=3)
    date=models.DateField(max_length=10)
    