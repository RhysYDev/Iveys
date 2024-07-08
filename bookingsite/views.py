from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.views import LoginView

# def index(request):
#     return HttpResponse("Welcome to the booking site!")

# def book(request):
#     return HttpResponse("Book a resource here.")

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  # Redirect authenticated users