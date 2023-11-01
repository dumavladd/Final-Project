from django.contrib.auth.models import User
from django.db import models


class Provider(models.Model):

    provider_name = models.CharField(max_length=50)
    cui = models.IntegerField()
    email = models.EmailField(max_length=50, null=True)
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.provider_name}'
