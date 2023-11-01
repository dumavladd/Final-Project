from django import forms
from django.forms import TextInput, EmailInput, NumberInput, DateInput, Select
from client.models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Please enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Please enter your email'}),
            'telephone': NumberInput(attrs={'class': 'form-control',
                                            'placeholder': 'Please enter your phone number'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'provider': Select(attrs={'class': 'form-select'}),

        }


class ClientUpdateForm(forms.ModelForm):
     class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Please enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Please enter your email'}),
            'telephone': NumberInput(attrs={'class': 'form-control',
                                            'placeholder': 'Please enter your phone number'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'provider': Select(attrs={'class': 'form-select'}),

        }
