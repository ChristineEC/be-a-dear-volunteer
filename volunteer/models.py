from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Beneficiary(models.Model):
    beneficiary_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    description = models.TextField(unique=True)
    location = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_beneficiaries")
    public_ok = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

# class Slot(model.Model):
#     beneficiary = models.ForeignKey(Beneficiary, CharField(max_length=150))