from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=250)
    manufacturer = models.CharField(max_length=250)
    price = models.FloatField()
    img_url = models.FileField()
