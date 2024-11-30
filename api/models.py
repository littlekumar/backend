from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=100)
    price = models.FloatField(max_length=32)
