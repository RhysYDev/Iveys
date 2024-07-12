from django.contrib import admin
from .models import User, Resource, Booking
from django_summernote.admin import SummernoteModelAdmin


# Register the Resource model
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'available')
    search_fields = ('name', 'description')
    list_filter = ('available',)

# Register the Booking model
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'resource', 'status')
    search_fields = ('user__username', 'resource__name', 'status')

# Models registered