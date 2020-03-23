from django.core.management.base import BaseCommand, CommandError
from shoes.models import ShoeType, ShoeColor
from manufacturer.models import Manufacturer

colors = [
    'RED', 'ORANGE', 'YELLOW',
    'GREEN', 'BLUE', 'INDIGO',
    'VIOLET', 'WHITE', 'BLACK'
]

shoe_types = [
    'Sneaker', 'Boot', 'Sandal',
    'Dress', 'Other'
]

manufacturer_names = [
    'Nike', 'Sketchers', 'Adidas',
    'Converse', 'New Balance'
]

class Command(BaseCommand):
    help = 'Pre-populate tables with shoe colors, types, and manufacturers'

    def _build_table(self):
        for idx, color in enumerate(colors):
            new_color = ShoeColor(idx, color)
            new_color.save()

        for idx, type in enumerate(shoe_types):
            new_type = ShoeType(idx, type)
            new_type.save()

        for idx, manufacturer in enumerate(manufacturer_names):
            new_manufacturer = Manufacturer(idx, manufacturer)
            new_manufacturer.save()

    def handle(self, *args, **kwargs):
        self._build_table()