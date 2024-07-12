from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone


class Resource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=False)
    phone_number = models.CharField(null=True, max_length=15)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    deadline_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled')
    ])
    commission_details = models.TextField()

    def __str__(self):
        return f"{self.commission_details} ({self.deadline_date})"
