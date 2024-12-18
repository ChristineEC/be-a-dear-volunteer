from django.db import models
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class About(models.Model):
    """
    The About model
    """
    title = models.CharField(max_length=50)
    content = models.TextField()
    featured_image = CloudinaryField('image', default="hearts")
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

    