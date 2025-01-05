# Generated by Django 4.2.16 on 2025-01-05 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0002_slot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_number', models.CharField(default=999, max_length=10)),
                ('class_year', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophmore'), ('JR', 'Junior'), ('SR', 'Senior'), ('UA', 'Unassigned')], max_length=10)),
            ],
            options={
                'ordering': ['classroom_number', 'class_year'],
            },
        ),
    ]
