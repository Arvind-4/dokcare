# Generated by Django 3.2.7 on 2021-09-18 15:23

import doctor.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=225)),
                ("email", models.EmailField(max_length=254)),
                ("date", models.DateTimeField(max_length=225)),
                ("phone_number", models.CharField(max_length=15)),
                ("content", models.TextField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name="DoctorJoin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=225)),
                ("email", models.EmailField(max_length=254)),
                (
                    "file_field",
                    models.FileField(
                        upload_to="documents/%Y/%m/%d",
                        validators=[doctor.validators.file_size],
                    ),
                ),
            ],
        ),
    ]
