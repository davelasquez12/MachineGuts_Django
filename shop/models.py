from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=250)
    manufacturer = models.CharField(max_length=250)
    price = models.FloatField()
    img_url = models.CharField(max_length=500)
    sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' - ' + self.manufacturer
