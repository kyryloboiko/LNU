from django.shortcuts import render
from .models import Attendance, Place, Event, Review
# Create your views here.


def places(request):  #The places page
    places = Place.objects.all()
    return render(request, 'main/places.html', {'places':places})

def events(request):  #The events page
    return render(request, 'main/events.html')