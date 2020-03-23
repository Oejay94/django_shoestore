from django.db import models

from manufacturer.models import Manufacturer

class ShoeType(models.Model):
    style = models.CharField(max_length=20)

    def __str__(self):
        return self.style

class ShoeColor(models.Model):
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Indigo = 'Indigo'
    Violet = 'Violet'
    White = 'White'
    Black = 'Black'
    color_choices = [
        (Red, 'Red'),
        (Orange, 'Orange'),
        (Yellow, 'Yellow'),
        (Green, 'Green'),
        (Blue, 'Blue'),
        (Indigo, 'Indigo'),
        (Violet, 'Violet'),
        (White, 'White'),
        (Black, 'Black')
    ]
    color_name = models.CharField(max_length=6, choices=color_choices, default=Red)

    def __str__(self):
        return self.color_name

class Shoe(models.Model):
    size = models.IntegerField()
    brand = models.CharField(max_length=20)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE, null=True)
    material = models.CharField(max_length=20)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE, null=True)
    fasten_type = models.CharField(max_length=20)
