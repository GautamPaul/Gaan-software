from django.db import models

# Create your models here.
class IOTEvent(models.Model):
    device = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=True)
    value = models.FloatField()
    source = models.CharField(max_length=50)
