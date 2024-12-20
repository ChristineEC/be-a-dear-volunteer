from django.db import models
from volunteer.models import Homeroom
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


PROFILE_TYPE = (
    (0, "Student"),
    (1, "Teacher"),
    (2, "School Admin"),
    )

# Create your models here.

class Profile(models.Model):

    """
    A profile to distinguish teachers from students and to
    assign users homerooms and aliases is created for each user
    related to the :model: auth.User
    and the :model: volunteer.Homeroom
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alias = models.CharField(max_length=15, unique=True)
    profile_pic = CloudinaryField('image', default='default-profile-pic.jpg')
    homeroom = models.ForeignKey(Homeroom, default="999", on_delete=models.SET_DEFAULT)
    profile_type = models.IntegerField(choices=PROFILE_TYPE, default=0)


    # class Meta:
    #     ordering = ["homeroom", "user"]

    def __str__(self):
        return f"{self.user.last_name}, {self.user.first_name}, alias {self.alias} | Room {self.homeroom.homeroom_number} | {self.homeroom.class_year}"
