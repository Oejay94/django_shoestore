from rest_framework import serializers

from .models import Shoe, ShoeColor, ShoeType
from manufacturer.models import Manufacturer

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = [
            'name',
            'website'
        ]

class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = [
            'size',
            'brand',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type'
        ]

class ShoeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = [
            'color_name'
        ]

class ShoeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeType
        fields = [
            'style'
        ]