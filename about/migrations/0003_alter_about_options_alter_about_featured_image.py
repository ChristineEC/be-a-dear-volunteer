# Generated by Django 4.2.16 on 2024-12-19 20:06

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_featured_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['status', 'updated_on']},
        ),
        migrations.AlterField(
            model_name='about',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='hearts.jpg', max_length=255, verbose_name='image'),
        ),
    ]
