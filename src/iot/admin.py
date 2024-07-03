from django.contrib import admin
from .models import IOTEvent

# Register your models here.

class IOTEventAdmin(admin.ModelAdmin):
    pass


admin.site.register(IOTEvent, IOTEventAdmin)