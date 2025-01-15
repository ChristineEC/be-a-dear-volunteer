# Generated by Django 4.2.16 on 2025-01-15 16:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_about_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='hearts2.jpg', max_length=255, verbose_name='image'),
        ),
    ]
