from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255)
    consultation_fees = models.DecimalField(max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr {self.name}"


class Patient(models.Model):
    name = models.CharField(max_length=255)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(
        max_length=255,
        choices=GENDER_CHOICES,
        default='M'
    )

    dob = models.DateField()
    email = models.EmailField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    BLOOD_GROUP_CHOICES = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    ]

    blood_group = models.CharField(
        max_length=3,
        choices=BLOOD_GROUP_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Patient {self.name}"


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    remarks = models.TextField(null=True, blank=True)

    APPOINTMENT_STATUS_CHOICES = [
        ("Completed", "Completed"),
        ("Pending", "Pending"),
        ("Cancelled", "Cancelled"),
    ]

    status = models.CharField(
        max_length=255,
        choices=APPOINTMENT_STATUS_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment {self.patient.name} with {self.doctor.name} at {self.date_time}"


class LabTest(models.Model):
    test_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.test_name

class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"


class AppointmentLabTest(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    lab_test = models.ForeignKey(LabTest, on_delete=models.CASCADE)

    result = models.CharField(max_length=255, null=True, blank=True)

    LAB_TEST_STATUS_CHOICES = [
        ("Completed", "Completed"),
        ("Pending", "Pending"),
    ]

    status = models.CharField(
        max_length=255,
        choices=LAB_TEST_STATUS_CHOICES
    )

    def __str__(self):
        return f"{self.appointment} - {self.lab_test}"



class Bill(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)

    doctor_fee = models.DecimalField(max_digits=10, decimal_places=2)
    lab_total = models.DecimalField(max_digits=10, decimal_places=2)
    medicine_total = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)

    PAYMENT_STATUS_CHOICES = [
        ("Paid", "Paid"),
        ("Unpaid", "Unpaid"),
    ]

    payment_status = models.CharField(
        max_length=255,
        choices=PAYMENT_STATUS_CHOICES
    )

    payment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Bill {self.id} - Appointment {self.appointment.id}"



class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)

    diagnosis = models.CharField(max_length=255)
    allergies = models.CharField(max_length=255, null=True, blank=True)
    medical_history = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Medical Record - {self.patient.name}"



class Medicine(models.Model):
    medicine_name = models.CharField(max_length=255)
    strength = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.medicine_name



class PrescriptionMedicine(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)

    dosage = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    instructions = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.prescription.id} - {self.medicine.medicine_name}"
