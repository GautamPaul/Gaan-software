from django.db import models

# Create your models here.
class IOTEvent(models.Model):
    event = models.TextField()
    time = models.DateTimeField()
    source = models.CharField()
    