from django.contrib import admin

from .models import ShoeType, ShoeColor, Shoe

admin.site.register(Shoe)
admin.site.register(ShoeType)
admin.site.register(ShoeColor)