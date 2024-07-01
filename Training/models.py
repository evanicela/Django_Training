from django.db import models


class Service(models.Model):
    image = models.ImageField(upload_to='services/')
    description = models.TextField()
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
