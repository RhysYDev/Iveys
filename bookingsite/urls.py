from django.urls import path
from . import views


urlpatterns = [
    path('nav/', views.NavigationView.as_view(), name='nav'),
    path('', views.EntryView.as_view(), name = 'home'),
]