from django.contrib import admin
from .models import Ambulance, EmergencyRequest


class AmbulanceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'vehicle_number',
        'driver_name',
        'ambulance_type',
        'status',
    )


admin.site.register(Ambulance, AmbulanceAdmin)


@admin.register(EmergencyRequest)
class EmergencyRequestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ambulance',
        'patient_name',
        'priority',
        'request_time',
        'status',
    )