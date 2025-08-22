from django.contrib import admin
from .models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['bilty_number', 'date', 'vehicle_number', 'driver_name',
                    'from_location', 'to_location', 'payment_status', 'profit']

    list_filter = ['payment_status', 'bill_status', 'pod_status', 'date']

    search_fields = ['bilty_number', 'vehicle_number', 'driver_name', 'client_name']

    fieldsets = (
        ('Basic Information', {
            'fields': ('date', 'bilty_number', 'vehicle_number')
        }),
        ('Driver Details', {
            'fields': ('driver_name', 'driver_mobile')
        }),
        ('Trip Details', {
            'fields': ('from_location', 'to_location', 'commodity', 'weight',
                       'adda_for_vehicle', 'adda_for_load', 'client_name', 'vendor')
        }),
        ('Financial Details', {
            'fields': ('amcs_rate', 'vehicle_rate', 'profit', 'adda_commission',
                       'staff_commission', 'loading_unloading')
        }),
        ('Payment Information', {
            'fields': ('fare_type', 'pod_status', 'bill_status', 'payment_status',
                       'payment_mode', 'cheque_details', 'advance', 'balance',
                       'receivable', 'payable')
        }),
    )

    readonly_fields = ['profit', 'balance']

    def save_model(self, request, obj, form, change):
        obj.save()
        super().save_model(request, obj, form, change)