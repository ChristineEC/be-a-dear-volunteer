from django.db import models
from django.contrib.auth.models import User
from volunteer.models import Homeroom

PROFILE_TYPE = (
    (0, "Student"),
    (1, "Teacher"),
    (2, "School Admin"),
    )

# # # Create your models here.

class Profile(models.Model):

    """
    A profile distinguishing teachers from students and
    assigning homerooms and aliases is created for each user
    related to the :model: auth.User
    and the :model: volunteer.Homeroom
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alias = models.CharField(max_length=15)
    homeroom = models.ForeignKey(Homeroom, blank=True, null=True, on_delete=models.CASCADE)
    profile_type = models.IntegerField(choices=PROFILE_TYPE, default=0)


    class Meta:
        ordering = ["homeroom", "user"]

    def __str__(self):
        return f"{self.user.username} | {self.user.alias} | {self.user.homeroom_number}"
