from django.contrib import admin

# Register your models here.

from .models import (
    Passenger,
    Flight,
    Reservation
)

admin.site.register(Passenger)
admin.site.register(Flight)
admin.site.register(Reservation)