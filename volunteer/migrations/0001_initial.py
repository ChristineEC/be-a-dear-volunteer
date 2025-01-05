# Generated by Django 4.2.16 on 2025-01-05 23:38

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiary_name', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(max_length=150)),
                ('short_description', models.CharField(default='', max_length=200)),
                ('description', models.TextField()),
                ('location', models.CharField(default='', max_length=255)),
                ('contact_details', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholderimage.jpg', max_length=255, verbose_name='image')),
            ],
            options={
                'ordering': ['beneficiary_name'],
            },
        ),
    ]
