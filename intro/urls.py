from django.urls import path

from intro import views

urlpatterns = [
    path('first-page/', views.index, name='first-page'),
]