from django.db import models

# Create your models here.
class IOTEvent(models.Model):
    device = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=True)
    value = models.FloatField()
    source = models.CharField(max_length=50)

    class Meta:
        verbose_name = "IOT Event"          # this is used to override model name, to display in admin panel

    def __str__(self):
        return f"{self.device}'s event at {self.time}"