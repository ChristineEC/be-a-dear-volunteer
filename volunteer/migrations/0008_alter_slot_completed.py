# Generated by Django 4.2.16 on 2025-01-07 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0007_alter_slot_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='completed',
            field=models.SmallIntegerField(choices=[(0, 'Completed'), (1, 'Incomplete')], default=0),
        ),
    ]
