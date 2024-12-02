from django.db import models


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class AboutProject(models.Model):
    """
    The AboutProject model
    """
    title = models.CharField(max_length=50)
    content = models.TextField(default="")
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
