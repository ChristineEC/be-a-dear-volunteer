# Generated by Django 4.2.16 on 2024-12-02 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiary',
            name='public_ok',
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
