from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.views import LoginView
from . import views

# def index(request):
#     return HttpResponse("Welcome to the booking site!")

# def book(request):
#     return HttpResponse("Book a resource here.")

class CustomLoginView(LoginView):
    template_name = 'bookingsite/login.html'
    redirect_authenticated_user = True

class NavigationView(generic.ListView):
    template_name = "bookingsite/index.html"

    def get_queryset(self):
        return []
    
class EntryView(generic.ListView):
    template_name = "bookingsite/entry.html"

    def get_queryset(self):
        return []