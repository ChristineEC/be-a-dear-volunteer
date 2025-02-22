# Generated by Django 4.2.16 on 2025-01-08 16:48

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('volunteer', '0002_alter_slot_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', cloudinary.models.CloudinaryField(default='default-profile-pic.jpg', max_length=255, verbose_name='image')),
                ('profile_type', models.PositiveSmallIntegerField(choices=[(0, 'Student'), (1, 'Teacher'), (2, 'SchoolAdmin')], default=0)),
                ('alias', models.CharField(default='Someone', max_length=25)),
                ('classroom', models.ForeignKey(default='999', on_delete=django.db.models.deletion.SET_DEFAULT, to='volunteer.classroom')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
