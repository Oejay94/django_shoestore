# Generated by Django 3.0.4 on 2020-03-20 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manufacturer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(choices=[('R', 'Red'), ('O', 'Orange'), ('Y', 'Yellow'), ('G', 'Green'), ('B', 'Blue'), ('I', 'Indigo'), ('V', 'Violet'), ('W', 'White'), ('BL', 'Black')], default='R', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('brand', models.CharField(max_length=20)),
                ('material', models.CharField(max_length=20)),
                ('fasten_type', models.CharField(max_length=20)),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shoes.ShoeColor')),
                ('manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manufacturer.Manufacturer')),
                ('shoe_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shoes.ShoeType')),
            ],
        ),
    ]
