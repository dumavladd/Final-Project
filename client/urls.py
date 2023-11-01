from client import views
from django.urls import path

urlpatterns = [
    path('create_client/', views.ClientCreateView.as_view(), name='create-client'),
    path('details_client/<int:pk>/', views.ClientDetailView.as_view(), name='details-client'),
    path('update_client/<int:pk>/', views.ClientUpdateView.as_view(), name='update-client'),
    path('delete_client/<int:pk>/', views.ClientDeleteView.as_view(), name='delete-client'),
    path('list_clients/', views.ClientListView.as_view(), name='list-of-clients'),
]
