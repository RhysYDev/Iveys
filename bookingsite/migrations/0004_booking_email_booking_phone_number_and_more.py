# Generated by Django 5.0.6 on 2024-07-12 11:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsite', '0003_alter_booking_user_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='deadline_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
