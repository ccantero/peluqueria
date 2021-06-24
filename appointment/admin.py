from django.contrib import admin

# Register your models here.
from . import models

# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('pk','user', 'create_date', 'appointment_date')

admin.site.register(models.Appointment, AppointmentAdmin)