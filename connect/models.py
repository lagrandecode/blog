from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=200)
    grade = models.CharField(max_length=50)
    cadre = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    age = models.IntegerField()


    
