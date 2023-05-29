from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Passenger(models.Model):

    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('0', 'Prefer Not To Say'),
    )


    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDERS, default='0')
    email = models.EmailField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Flight(models.Model):

    AIRLINES = (
        ('THY', 'Turkish Airlines'),
        ('EMR', 'Emirates Airlines'),
        ('SWS', 'Swiss International Airlines'),
    )

    COUNTRIES = (
        (1, 'Adana'),
        (7, 'Antalya'),
        (16, 'Bursa'),
        (34, 'Istanbul'),
        (35, 'Izmir'),
    )


    flight_number = models.CharField(max_length=64)
    airline = models.CharField(max_length=3, choices=AIRLINES, default='THY')
    departure = models.PositiveSmallIntegerField(choices=COUNTRIES)
    departure_time = models.DateField()
    arrival = models.PositiveSmallIntegerField(choices=COUNTRIES)
    arrival_time = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    