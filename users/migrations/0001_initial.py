# Generated by Django 4.2.16 on 2024-12-13 02:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('volunteer', '0002_alter_homeroom_class_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=15)),
                ('profile_type', models.IntegerField(choices=[(0, 'Student'), (1, 'Teacher'), (2, 'School Admin')], default=0)),
                ('homeroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='volunteer.homeroom')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['homeroom', 'user'],
            },
        ),
    ]