from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from provider.filters import ProviderFilter
from provider.forms import ProviderForm, ProviderUpdateForm
from provider.models import Provider


class ProviderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'provider/create_provider.html'
    model = Provider
    form_class = ProviderForm
    success_url = reverse_lazy('list-of-providers')
    success_message = 'Provider {cname} {cui} a fost adaugat cu succes. Adresa de email este: {email}.'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(cname=self.object.company_name, cui=self.object.cui, email=self.object.email)

    def form_valid(self, form):
        if form.is_valid():
            new_provider = form.save(commit=False)
            new_provider.user = self.request.user
            new_provider.save()

        return redirect('list-of-providers')





class ProviderDetailView(LoginRequiredMixin, DetailView):  # ReadView
    template_name = 'provider/details_provider.html'
    model = Provider


class ProviderUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'provider/update_provider.html'
    model = Provider
    form_class = ProviderUpdateForm
    success_url = reverse_lazy('list-of-providers')

    def form_valid(self, form):
        if form.is_valid():
            update_provider = form.save(commit=False)
            update_provider.user = self.request.user
            update_provider.save()

        return redirect('list-of-providers')


class ProviderDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'provider/delete_provider.html'
    model = Provider
    success_url = reverse_lazy('list-of-providers')


class ProviderListView(LoginRequiredMixin, ListView):
    template_name = 'provider/list_of_providers.html'
    model = Provider
    context_object_name = 'all_providers'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Provider.objects.all()
        else:
            return Provider.objects.filter(user_id=self.request.user.id)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_superuser:
            get_all_providers = Provider.objects.all()
        else:
            get_all_providers = Provider.objects.filter(user_id=self.request.user.id)

        filters = ProviderFilter(self.request.GET, queryset=get_all_providers)
        context['all_providers'] = filters.qs
        context['form_filters'] = filters.form
        return context
