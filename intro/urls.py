from django.urls import path

from intro import views

urlpatterns = [
    path('first_page/', views.index, name=''),
]