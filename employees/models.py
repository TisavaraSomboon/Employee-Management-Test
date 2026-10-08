import os
from django.db import models
from django.conf import settings

images_path = str(os.path.join(settings.LOCAL_FILE_DIR, "images"))

class Status(models.TextChoices):
    RECRUITMENT_PROCESS = "recruitment_process", "In recruitment process"
    WAITING_ONBOARDING = "waiting_onboarding", "Waiting for onboarding"
    PROBATION = "probation", "In probation period"
    NORMAL = "normal", "Normal"
    RESIGNED = "resigned", "Resigned"

class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    manager = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="employees",
    )
    image = models.FilePathField(path=images_path)
    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.RECRUITMENT_PROCESS,
    )
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Position(models.Model):
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=12, decimal_places=2)

class Department(models.Model):
    name = models.CharField(max_length=100)
    manager = models.OneToOneField(
        "Employee",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_department",
    )

    def __str__(self):
        return self.name