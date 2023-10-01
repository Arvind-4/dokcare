from django.db import models

from .validators import file_size

# Create your models here.


class Appointment(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    date = models.DateTimeField(max_length=225)
    phone_number = models.CharField(max_length=15)
    content = models.TextField(max_length=225)

    def __str__(self):
        return self.name


class DoctorJoin(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    file_field = models.FileField(
        upload_to="documents/%Y/%m/%d", validators=[file_size]
    )

    def __str__(self):
        return self.name
