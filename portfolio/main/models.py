from django.db import models


class Main (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    technology = models.CharField(max_length=30)
    image = models.FileField(upload_to='img/')