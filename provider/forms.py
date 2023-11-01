from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, Select

from provider.models import Provider


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        exclude = ['user']

        widgets = {
            'provider_name': TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Please enter your provider name'}),
            'cui': NumberInput(attrs={'class': 'form-control',
                                      'placeholder': 'Please enter your registration number'}),
            'email': EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Please enter your email'}),
            'description': Textarea(attrs={'class': 'form-control',
                                           'placeholder': 'Please write your description', 'rows': 6}),
            'user': Select(attrs={'class': 'form-select'}),

        }


class ProviderUpdateForm(forms.ModelForm):
    class Meta:
        model = Provider
        exclude = ['user']
        widgets = {
            'provider_name': TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Please enter your provider name'}),
            'cui': NumberInput(attrs={'class': 'form-control',
                                      'placeholder': 'Please enter your registration number'}),
            'email': EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Please enter your email'}),
            'description': Textarea(attrs={'class': 'form-control',
                                           'placeholder': 'Please write your description', 'rows': 6}),
            'user': Select(attrs={'class': 'form-select'}),

        }
