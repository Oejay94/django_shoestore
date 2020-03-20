from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=15)
    website = models.URLField()
