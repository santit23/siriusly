from django.db import models
from django.urls import reverse

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length=50)

    def __str__(self):
        return self.image_name

    def get_absolute_url(self):
        return reverse("redirect")
    