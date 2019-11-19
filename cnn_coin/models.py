from django.db import models

# Create your models here.
class ImageModel(models.Model):
    image = models.ImageField(null = False)

    def __str__(self):
        return self.image.url
        