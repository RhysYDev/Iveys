from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import LoginView
from . import views

class NavigationView(generic.ListView):
    template_name = "bookingsite/index.html"

    def get_queryset(self):
        return []
    
class EntryView(generic.ListView):
    template_name = "bookingsite/entry.html"

    def get_queryset(self):
        return []