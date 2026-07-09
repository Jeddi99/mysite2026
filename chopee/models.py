from django.db import models

# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length=400)
    name = models.CharField(max_length=400)
    price = models.FloatField()
    year = models.IntegerField()