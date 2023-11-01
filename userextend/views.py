import datetime

from django.contrib.auth.models import User
from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView

from membership.models import UserMembership, Membership
from userextend.forms import UserForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')


    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save()
            start_date = datetime.datetime.now().date()
            end_date = (datetime.datetime.now() + datetime.timedelta(days=365)).date()
            UserMembership.objects.create(user=new_user,
                                          membership=Membership.objects.get(type=self.request.GET.get('m')),
                                          start_date=start_date,
                                          end_date=end_date),


            return redirect('login')
        else:
            return redirect('homepage')