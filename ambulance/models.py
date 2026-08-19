from django.db import models


class Ambulance(models.Model):

    AMBULANCE_TYPE_CHOICES = [
        ("Basic Life Support", "Basic Life Support"),
        ("Advanced Life Support", "Advanced Life Support"),
        ("Patient Transport", "Patient Transport"),
    ]

    STATUS_CHOICES = [
        ("available", "Available"),
        ("busy", "Busy"),
    ]

    vehicle_number = models.CharField(max_length=255)
    driver_name = models.CharField(max_length=255)
    ambulance_type = models.CharField(
        max_length=255,
        choices=AMBULANCE_TYPE_CHOICES
    )
    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES
    )

    def __str__(self):
        return f"{self.vehicle_number} - {self.driver_name}"




class EmergencyRequest(models.Model):

    PRIORITY_CHOICES = [
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("dispatched", "Dispatched"),
        ("completed", "Completed"),
    ]

    ambulance = models.ForeignKey(
        Ambulance,
        on_delete=models.CASCADE
    )

    patient_name = models.CharField(max_length=255)

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES
    )

    request_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    def __str__(self):
        return f"{self.patient_name} - {self.priority}"
