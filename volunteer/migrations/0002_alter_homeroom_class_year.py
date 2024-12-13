# Generated by Django 4.2.16 on 2024-12-13 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeroom',
            name='class_year',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophmore'), ('JR', 'Junior'), ('SR', 'Senior'), ('UA', 'Unassigned')], max_length=10),
        ),
    ]
