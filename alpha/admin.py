from django.contrib import admin
from .models import Doctor, Patient, Appointment, LabTest, Prescription, AppointmentLabTest,  Bill, MedicalRecord,  Medicine, PrescriptionMedicine
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'email', 'phone', 'consultation_fees', 'created_at', 'updated_at')
    list_filter = ('specialization', 'consultation_fees')
    search_fields = ('name',)
admin.site.register(Doctor, DoctorAdmin)


# Register Patient Model
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'dob', 'email', 'address', 'blood_group', 'created_at', 'updated_at')
    list_filter = ('blood_group', 'gender')
    search_fields = ('name',)
admin.site.register(Patient, PatientAdmin)


# Register Appointment Model
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'remarks', 'status', 'created_at', 'updated_at')

admin.site.register(Appointment, AppointmentAdmin)

# Lab test Models
class LabTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_name', 'price', 'description')

admin.site.register(LabTest, LabTestAdmin)



# Register Prescription Model
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment', 'notes', 'created_at', 'updated_at')
    search_fields = ('notes',)

admin.site.register(Prescription, PrescriptionAdmin)


# Register AppointmentLabTest Model
class AppointmentLabTestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'appointment',
        'lab_test',
        'result',
        'status'
    )


admin.site.register(AppointmentLabTest, AppointmentLabTestAdmin)



# Register Bill Model
class BillAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'appointment',
        'doctor_fee',
        'lab_total',
        'medicine_total',
        'discount',
        'tax',
        'grand_total',
        'payment_status',
        'payment_date'
    )


admin.site.register(Bill, BillAdmin)



# Register MedicalRecord Model
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'patient',
        'appointment',
        'diagnosis',
        'allergies',
        'medical_history',
        'notes',
        'created_at'
    )


admin.site.register(MedicalRecord, MedicalRecordAdmin)



# Register Medicine Model
class MedicineAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'medicine_name',
        'strength',
        'price',
        'stock'
    )


admin.site.register(Medicine, MedicineAdmin)


# Register PrescriptionMedicine Model
class PrescriptionMedicineAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'prescription',
        'medicine',
        'dosage',
        'frequency',
        'duration',
        'instructions',
    )


admin.site.register(PrescriptionMedicine, PrescriptionMedicineAdmin)




