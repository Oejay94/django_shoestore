from django.shortcuts import render

from .models import Manufacturer

def manufacturer_view(request):
    html = 'manufacturer.html'
    return render(request, html, {'mans': Manufacturer.objects.all()})