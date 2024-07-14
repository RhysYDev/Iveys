from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.views import LoginView
from . import views
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking, Resource
from .forms import BookingForm


class NavigationView(generic.ListView):
    template_name = "bookingsite/index.html"

    def get_queryset(self):
        return []
    
class EntryView(generic.ListView):
    template_name = "bookingsite/entry.html"

    def get_queryset(self):
        return []

class BookingView(generic.ListView):
    template_name = "bookingsite/booking.html"

    def get_queryset(self):
        return []

class InkworkView(generic.ListView):
    template_name = "bookingsite/inkwork.html"

    def get_queryset(self):
        return []

class PaintworkView(generic.ListView):
    template_name = "bookingsite/paintwork.html"

    def get_queryset(self):
        return []

class DigiworkView(generic.ListView):
    template_name = "bookingsite/digiwork.html"

    def get_queryset(self):
        return []

class LenseworkView(generic.ListView):
    template_name = "bookingsite/lensework.html"

    def get_queryset(self):
        return []

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.add_message(request, messages.SUCCESS, "Booking successfully sent!")
            return redirect('show_booking', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'bookingsite/booking.html', {'form': form})

@login_required
def edit_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Booking successfully edited!")
            return redirect('show_booking', booking_id=booking.id)
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookingsite/edit_booking.html', {'form': form, 'booking': booking})

@login_required
def delete_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    if request.method == 'POST':
        booking.delete()
        messages.add_message(request, messages.SUCCESS, "Booking successfully deleted!")
        return redirect('show_all_booking')
    return render(request, 'bookingsite/delete_booking.html', {'booking': booking})

@login_required
def show_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    return render(request, 'bookingsite/show_booking.html', {'booking': booking})

@login_required
def show_all_booking(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookingsite/show_all_booking.html', {'bookings': bookings})

@login_required
def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'home/booking_success.html', {'booking': booking})