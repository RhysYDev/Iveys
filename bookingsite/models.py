from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    phone_number = models.CharField(max_length=15)


class Resource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled')
    ])
    payment_details = models.TextField()


# class Payment(models.Model):
#     booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_date = models.DateTimeField()
#     payment_method = models.CharField(max_length=50)


# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
#     rating = models.IntegerField()
#     comments = models.TextField()


# class Schedule(models.Model):
#     resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     date = models.DateField()