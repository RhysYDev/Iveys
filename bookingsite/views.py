from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the booking site!")

def book(request):
    return HttpResponse("Book a resource here.")