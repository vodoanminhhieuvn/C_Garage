from django import forms
from .models import Car

class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['owner', 'address', 'license_plate', 'phone_number', 'email', 'car_brand', 'is_edited']
    is_edited = forms.BooleanField(widget=forms.TextInput(attrs={'readonly':'readonly'}))