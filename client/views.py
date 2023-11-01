from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from client.filters import ClientFilter
from client.forms import ClientForm, ClientUpdateForm
from client.models import Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    template_name = 'client/create_client.html'
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('list-of-clients')
    success_message = 'Client {fname} {lname} a fost adaugat cu succes. Adresa de email este: {email}.'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(fname=self.object.first_name, lname=self.object.last_name, email=self.object.email)


class ClientDetailView(LoginRequiredMixin, DetailView):
    template_name = 'client/details_client.html'
    model = Client


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'client/update_client.html'
    model = Client
    form_class = ClientUpdateForm
    success_url = reverse_lazy('list-of-clients')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'client/delete_client.html'
    model = Client
    success_url = reverse_lazy('list-of-clients')


class ClientListView(LoginRequiredMixin, ListView):
    template_name = 'client/list_of_clients.html'
    model = Client
    context_object_name = 'all_clients'

    def get_queryset(self):
        return Client.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_clients = [client.id for client in Client.objects.filter(provider__user_id=self.request.user.id)]
        context['my_clients'] = my_clients

        get_all_clients = Client.objects.all()
        filters = ClientFilter(self.request.GET, queryset=get_all_clients)
        context['all_clients'] = filters.qs
        context['form_filters'] = filters.form
        return context