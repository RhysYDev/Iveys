# Generated by Django 5.0.6 on 2024-07-11 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='payment_details',
            new_name='commission_details',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='booking_date',
            new_name='deadline_date',
        ),
    ]
