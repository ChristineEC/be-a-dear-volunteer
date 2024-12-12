# from django.db import models
# from django.contrib.auth.models import User, Homeroom

# PROFILE_TYPE = ((0, "Student"), (1, "Teacher"),(2, "School Admin") )
# CLASS_YEARS = (
#     ("FR", "Freshman"),
#     ("SO", "Sophmore"),
#     ("JR", "Junior"),
#     ("SR", "Senior"),
#     ("UA", "Unassigned")
#     )


# # Create your models here.
# class Homeroom(models.Model):
#     homeroom_number = models.CharField(max_length=10, unique=True)
#     class_year = models.CharField(max_length=4, choices=CLASS_YEARS, default="FR")

#     def _str__(self):
#         return f"{self.homeroom_number} | Class Year: {self.class_year}"


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     alias = models.CharField(max_length=15)
#     homeroom_number = models.ForeignKey(Homeroom, on_delete=models.PROTECT)
#     profile_type = models.IntegerField(choices=PROFILE_TYPE, default=0)

#     def __str__(self):
#         return f"{self.user.username}"
