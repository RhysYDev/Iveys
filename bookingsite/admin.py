from django.contrib import admin
from .models import User, Resource, Booking
from django_summernote.admin import SummernoteModelAdmin

# Register the User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')

# Register the Resource model
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'available')
    search_fields = ('name', 'description')
    list_filter = ('available',)

# Register the Booking model
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'resource', 'booking_date', 'status')
    search_fields = ('user__username', 'resource__name', 'status')
    list_filter = ('status', 'booking_date')

# Models registered