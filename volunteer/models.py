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
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

# class Slot(models.Model):
#     beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, related_name="slots")
#     task = models.CharField(max_length="200")
#     special_reqs = models.CharField(max_length=100, default="")
#     date = models.DateTimeField(blank=True)
#     start_time = models.TimeField(blank=True)
#     end_time = models.TimeField(blank=True)
#     custom = models.BooleanField(default=True)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     reserved_by = model.ForeignKey(Student)
#     completed_on = models.DateTimeField(blank=True, )
