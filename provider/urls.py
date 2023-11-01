from django.urls import path
from provider import views

urlpatterns = [
    path('create_provider/', views.ProviderCreateView.as_view(), name='create-provider'),
    path('details_provider/<int:pk>/', views.ProviderDetailView.as_view(), name='details-provider'),
    path('update_provider/<int:pk>/', views.ProviderUpdateView.as_view(), name='update-provider'),
    path('delete_provider/<int:pk>/', views.ProviderDeleteView.as_view(), name='delete-provider'),
    path('list_of_providers/', views.ProviderListView.as_view(), name='list-of-providers'),
]