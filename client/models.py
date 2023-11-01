from django.db import models

from provider.models import Provider


class Client(models.Model):

    first_name = models.CharField(max_length=31, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=50, null=True)
    telephone = models.IntegerField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile = models.ImageField(upload_to='profiles/', null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
