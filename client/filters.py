import django_filters

from django import forms
from provider.models import Provider
from client.models import Client


class ClientFilter(django_filters.FilterSet):

    list_of_clients = [(provider.id, f'{provider.provider_name}') for provider in Provider.objects.all()]
    provider = django_filters.ChoiceFilter(choices=list_of_clients, widget=forms.Select(attrs={'class': 'form-select'}))

    start_date_gte = (django_filters.DateFilter
                      (field_name='start_date', lookup_expr='gte', widget=forms.DateInput
                      (attrs={'class': 'form-control', 'type': 'date'})))
    start_date_lte = (django_filters.DateFilter
                      (field_name='start_date', lookup_expr='lte', widget=forms.DateInput
                      (attrs={'class': 'form-control', 'type': 'date'})))

    first_name = django_filters.CharFilter(lookup_expr='icontains', label='First name',
                                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Last name',
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = django_filters.CharFilter(lookup_expr='icontains', label='Email',
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'telephone',
                  'start_date_gte', 'start_date_lte', 'provider',]
