from django.contrib import admin

from .models import Appointment, DoctorJoin

# Register your models here.

admin.site.register(Appointment)
admin.site.register(DoctorJoin)
