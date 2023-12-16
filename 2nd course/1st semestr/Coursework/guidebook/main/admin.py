from django.contrib import admin
from .models import Place, Event, Review, Attendance
# Register your models here.

admin.site.register(Place)
admin.site.register(Event)
admin.site.register(Review)
admin.site.register(Attendance)