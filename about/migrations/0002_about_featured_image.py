# Generated by Django 4.2.16 on 2024-12-18 23:01

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='hearts', max_length=255, verbose_name='image'),
        ),
    ]
