from django.db import models
from django.contrib.auth.models import User
from volunteer.models import Classroom
from cloudinary.models import CloudinaryField


PROFILE_TYPE = (
    (0, "Student"),
    (1, "Teacher"),
    (2, "SchoolAdmin"),
)


class Profile(models.Model):
    """
    Stores a single entry of profile related to
    :model: auth.User and
    :model: Homeroom.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image', default='placeholder')
    classroom = models.ForeignKey(Classroom, default="999",
                                  on_delete=models.SET_DEFAULT)
    profile_type = models.PositiveSmallIntegerField(
                                                    choices=PROFILE_TYPE,
                                                    default=0)
    alias = models.CharField(max_length=25, default="Someone")
