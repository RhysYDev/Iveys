from django.urls import path
from . import views


urlpatterns = [
    path('nav/', views.NavigationView.as_view(), name='nav'),
    path('', views.EntryView.as_view(), name = 'home'),
    path('booking/', views.BookingView.as_view(), name = 'booking')
]