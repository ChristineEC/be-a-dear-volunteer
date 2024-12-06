# Generated by Django 4.2.16 on 2024-12-01 14:50

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
                ('beneficiary_name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('description', models.TextField(unique=True)),
                ('location', models.CharField(max_length=255)),
                ('contact_details', models.CharField(max_length=200)),
                ('public_ok', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_beneficiaries', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
