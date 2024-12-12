from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Beneficiary(models.Model):
    beneficiary_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    description = models.TextField(unique=True)
    location = models.CharField(max_length=255, default="")
    contact_details = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

class Slot(models.Model):
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.PROTECT, related_name="slots")
    task = models.CharField(max_length=200, default="")
    task_location = models.CharField(max_length=200, default="")
    date = models.DateTimeField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    reserved_by = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name="reservations")
    completed = models.BooleanField(default=False)
    credit_minutes_requested = models.IntegerField(default=0)
    teacher_approved = models.BooleanField(default=False)
    publish_ok = models.BooleanField(default=False)
