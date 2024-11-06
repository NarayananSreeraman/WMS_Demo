# forms.py in your Django app (e.g., 'app1')

from django import forms
from .models import WasteRequest

class WasteRequestForm(forms.ModelForm):
    class Meta:
        model = WasteRequest
        fields = ['waste_type', 'quantity', 'scheduled_time', 'location']
        widgets = {
            'scheduled_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
