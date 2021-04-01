from django.db import models

# Create your models here.
class Media(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.title