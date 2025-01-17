from django.db import models
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class About(models.Model):
    """
    Stores a single entry of about
    """
    title = models.CharField(max_length=50)
    content = models.TextField()
    featured_image = CloudinaryField('image', default="placeholder")
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["status", "updated_on"]

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Stores a single entry of collaboraterequest
    """
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'Collaboration request from {self.name}'
