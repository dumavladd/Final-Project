from django.urls import path

from home import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='homepage'),
    path('team/', views.TeamTemplateView.as_view(), name='team'),
    path('stuff/', views.StuffTemplateView.as_view(), name='stuff'),
    path('resource/', views.ResourceTemplateView.as_view(), name='resource'),
    path('privacy/', views.PrivacyTemplateView.as_view(), name='privacy'),
    path('location/', views.LocationTemplateView.as_view(), name='location'),
    path('cv/', views.CvTemplateView.as_view(), name='cv'),
]