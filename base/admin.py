from django.contrib import admin
from .models import Customer, Record, Room, Roomtype

admin.site.register(Customer)
admin.site.register(Room)
admin.site.register(Roomtype)
admin.site.register(Record)
