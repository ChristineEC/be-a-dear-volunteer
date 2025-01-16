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
    A profile to be able to assign users
    to homerooms, distinguish teachers and school admins
    from students, and allow students to choose an alias.
    The model is related to
    :model: User, and, together with the
    :model: Homeroom, will enable comparison of homeroom
    stats regarding volunteer hours.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image', default='placeholder')
    classroom = models.ForeignKey(Classroom, default="999",
                                  on_delete=models.SET_DEFAULT)
    profile_type = models.PositiveSmallIntegerField(
                                                    choices=PROFILE_TYPE,
                                                    default=0)
    alias = models.CharField(max_length=25, default="Someone")
