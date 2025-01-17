from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = (
    (0, "Draft"),
    (1, "Published")
    )

CLASS_YEARS = (
    ("FR", "Freshman"),
    ("SO", "Sophmore"),
    ("JR", "Junior"),
    ("SR", "Senior"),
    ("UA", "Unassigned"),
    )

COMPLETION = (
    (0, "Incomplete"),
    (1, "Completed"),
)


# Create your models here.

class Beneficiary(models.Model):
    """
    Stores a single beneficiary.
    """
    beneficiary_name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150)
    short_description = models.CharField(max_length=255, default="")
    description = models.TextField()
    location = models.CharField(max_length=255, default="")
    contact_details = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["beneficiary_name"]


class Slot(models.Model):
    """
    Stores a single slot related to :model: Beneficiary
    and :model: auth.User
    """
    beneficiary = models.ForeignKey(Beneficiary,
                                    on_delete=models.CASCADE,
                                    related_name="slots")
    task = models.CharField(max_length=200, default="")
    task_location = models.CharField(max_length=200,
                                     default="(use pseudonym "
                                     "for private beneficiary)")
    dates = models.CharField(max_length=200, default="to be determined")
    times = models.CharField(max_length=200, default="to be determined")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    reserved_by = models.ForeignKey(User, blank=True,
                                    on_delete=models.CASCADE,
                                    related_name="reservations")
    completed = models.SmallIntegerField(choices=COMPLETION, default=0)
    credit_minutes_requested = models.SmallIntegerField(default=0)
    credit_minutes_approved = models.SmallIntegerField(default=0)
    publish_ok = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]


class Classroom(models.Model):
    """
    Stores a single classroom entry.
    """
    classroom_number = models.CharField(max_length=10, primary_key=True)
    class_year = models.CharField(max_length=10, choices=CLASS_YEARS)

    class Meta:
        app_label = "volunteer"
        ordering = ["classroom_number", "class_year"]
