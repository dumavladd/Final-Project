import django_filters
from django import forms

from provider.models import Provider



class ProviderFilter(django_filters.FilterSet):

    provider_name = django_filters.CharFilter(lookup_expr='icontains', label='Provider name',
                                           widget=forms.TextInput(attrs={'class': 'form-control'}))

    cui = django_filters.CharFilter(lookup_expr='icontains', label='Cui',
                                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = django_filters.CharFilter(lookup_expr='icontains', label='Email',
                                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Provider
        exclude = ['image', 'user']
