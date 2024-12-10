from django.db import models
from django.contrib.auth.models import User

PROFILE_TYPE = ((0, "Student"), (1, "Teacher"))
CLASS_YEARS = (
    ("FR", "Freshman"),
    ("SO", "Sophmore"),
    ("JR", "Junior"),
    ("SR", "Senior"),
    )


# Create your models here.
class Homeroom(models.Model):
    room_num = models.CharField(max_length=5, unique=True)
    class_year = models.CharField(max_length=4, choices=CLASS_YEARS, default="FR")

    def _str__(self):
        return self.room_num


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    alias = models.CharField(max_length=15)
    homeroom = models.ForeignKey(Homeroom, on_delete=models.PROTECT)
    photo_permission = models.BooleanField(default=False)
    profile_type = models.IntegerField(choices=PROFILE_TYPE, default=0)

    def __str__(self):
        return str(self.user + self.profile_type)




