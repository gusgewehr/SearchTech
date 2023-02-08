from django.db import models

# Create your models here.
class Drive(models.Model):
    name = models.TextField(max_length=500)
    file = models.FileField(upload_to='drive')