from django.shortcuts import render, get_object_or_404
from .models import Attendance, Place, Event, Review
# Create your views here.


def places(request):  #The places page
    places = Place.objects.all()
    return render(request, 'main/places.html', {'places':places})

def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    # Тут можна передати додаткові дані у шаблон, якщо потрібно
    return render(request, 'main/place_detail.html', {'place': place})

def events(request):  #The events page
    events = Event.objects.all()
    return render(request, 'main/events.html', {'events':events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    # Тут можна передати додаткові дані у шаблон, якщо потрібно
    return render(request, 'main/event_detail.html', {'event': event})