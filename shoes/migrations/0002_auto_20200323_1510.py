# Generated by Django 3.0.4 on 2020-03-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoecolor',
            name='color_name',
            field=models.CharField(choices=[('Red', 'Red'), ('Orange', 'Orange'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Blue', 'Blue'), ('Indigo', 'Indigo'), ('Violet', 'Violet'), ('White', 'White'), ('Black', 'Black')], default='Red', max_length=6),
        ),
    ]
