from django.urls import path
from . import views


urlpatterns = [
    path('nav/', views.NavigationView.as_view(), name='nav'),
    path('', views.EntryView.as_view(), name = 'home'),
    path('booking/', views.BookingView.as_view(), name = 'booking'),
    path('create/', views.create_booking, name='create_booking'),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('<int:booking_id>/', views.show_booking, name='show_booking'),
    path('show_all/', views.show_all_booking, name='show_all_booking'),
    path('booking-success/<int:booking_id>/', views.booking_success, name='booking-success'),
    path('inkwork/', views.InkworkView.as_view(), name='inkwork'),
    path('digiwork/', views.DigiworkView.as_view(), name='digiwork'),
    path('paintwork/', views.PaintworkView.as_view(), name='paintwork'),
    path('lensework/', views.LenseworkView.as_view(), name='lensework'),
]