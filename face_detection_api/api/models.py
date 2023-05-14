from django.db import models

class Picture(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='in')
