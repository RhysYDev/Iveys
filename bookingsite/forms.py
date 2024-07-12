from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('resource', 'deadline_date', 'commission_details', 'email', 'phone_number')
        exclude = ['user']
        widgets = {
            'deadline_date': forms.DateInput(attrs={'type': 'date'})
        }