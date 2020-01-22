from django.db import models


# Create your models here.

class Exhibit(models.Model):
    exhibit_title = models.CharField(max_length=200)
    exhibit_description = models.TextField()
    exhibit_picture = models.ImageField(upload_to="gallery")
    

