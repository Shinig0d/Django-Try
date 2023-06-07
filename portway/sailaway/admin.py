from django.contrib import admin

from .models import Port, Sailaway, Passenger

# Register your models here.
admin.site.register(Port)
admin.site.register(Sailaway)
admin.site.register(Passenger)