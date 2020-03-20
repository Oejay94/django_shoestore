from django.db import models

from manufacturer.models import Manufacturer

class ShoeType(models.Model):
    style = models.CharField(max_length=20)

class ShoeColor(models.Model):
    pass

class Shoe(models.Model):
    size = models.IntegerField()
    brand = models.CharField(max_length=20)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE, null=True)
    material = models.CharField(max_length=20)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE, null=True)
    fasten_type = models.CharField(max_length=20)
