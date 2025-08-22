from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'
        exclude = ['profit', 'balance']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'bilty_number': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., TKN-291'}),
            'driver_name': forms.TextInput(attrs={'class': 'form-control'}),
            'driver_mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 0308-2650585'}),
            'from_location': forms.TextInput(attrs={'class': 'form-control'}),
            'to_location': forms.TextInput(attrs={'class': 'form-control'}),
            'commodity': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'adda_for_vehicle': forms.TextInput(attrs={'class': 'form-control'}),
            'adda_for_load': forms.TextInput(attrs={'class': 'form-control'}),
            'client_name': forms.TextInput(attrs={'class': 'form-control'}),
            'vendor': forms.TextInput(attrs={'class': 'form-control'}),
            'amcs_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'vehicle_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'adda_commission': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'staff_commission': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'loading_unloading': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fare_type': forms.Select(attrs={'class': 'form-control'}),
            'pod_status': forms.Select(attrs={'class': 'form-control'}),
            'bill_status': forms.Select(attrs={'class': 'form-control'}),
            'payment_status': forms.Select(attrs={'class': 'form-control'}),
            'payment_mode': forms.Select(attrs={'class': 'form-control'}),
            'cheque_details': forms.TextInput(attrs={'class': 'form-control'}),
            'advance': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'receivable': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'payable': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }