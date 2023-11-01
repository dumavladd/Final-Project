from django.contrib.auth.models import User
from django.db import models

class Membership(models.Model):
    list_of_currency = (
        ('$', 'Dollar'),
        ('€', 'Euro'),
        ('RON', 'Ron')
    )
    type = models.CharField(max_length=20)
    description = models.TextField(max_length=400)
    price = models.IntegerField()
    currency = models.CharField(max_length=3, choices=list_of_currency)
    color = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.type


class UserMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.user.username} -> {self.membership.type}"
