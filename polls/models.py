from django.db import models

# Create your models here.


class Person(models.Model):
    id = models.CharField(max_length=255, unique=True, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)