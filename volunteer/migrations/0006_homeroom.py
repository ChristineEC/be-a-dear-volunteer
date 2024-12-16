# Generated by Django 4.2.16 on 2024-12-15 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0005_alter_slot_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homeroom',
            fields=[
                ('homeroom_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('class_year', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophmore'), ('JR', 'Junior'), ('SR', 'Senior'), ('UA', 'Unassigned')], max_length=10)),
            ],
            options={
                'ordering': ['homeroom_number', 'class_year'],
            },
        ),
    ]