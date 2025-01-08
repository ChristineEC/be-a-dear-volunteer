# Generated by Django 4.2.16 on 2025-01-08 16:31

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('classroom_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('class_year', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophmore'), ('JR', 'Junior'), ('SR', 'Senior'), ('UA', 'Unassigned')], max_length=10)),
            ],
            options={
                'ordering': ['classroom_number', 'class_year'],
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(default='', max_length=200)),
                ('task_location', models.CharField(default='use pseudonym for private beneficiary)', max_length=200)),
                ('dates', models.CharField(default='to be determined', max_length=200)),
                ('times', models.CharField(default='to be determined', max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('completed', models.SmallIntegerField(choices=[(0, 'Completed'), (1, 'Incomplete')], default=0)),
                ('credit_minutes_requested', models.SmallIntegerField(default=0)),
                ('credit_minutes_approved', models.SmallIntegerField(default=0)),
                ('publish_ok', models.BooleanField(default=False)),
                ('beneficiary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='volunteer.beneficiary')),
                ('reserved_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
