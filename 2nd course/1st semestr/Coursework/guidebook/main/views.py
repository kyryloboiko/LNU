from django.shortcuts import render, get_object_or_404, redirect
from .models import Attendance, Place, Event, Review
from datetime import datetime
from django.utils import timezone
from .forms import EventForm
from .forms import ReviewForm
# Create your views here.


def places_page(request):
    places = Place.objects.all()

    # Отримання параметрів фільтрації з URL
    county = request.GET.get('county')
    city = request.GET.get('city')
    region = request.GET.get('region')
    kind = request.GET.get('kind')
    type = request.GET.get('type')
    min_score = request.GET.get('min_score')
    max_score = request.GET.get('max_score')
    order_by = request.GET.get('order_by')  # Може бути 'asc' або 'desc'
    search = request.GET.get('search')  # Параметр пошуку по назві

    # Фільтрація за параметрами, якщо вони існують
    if county:
        places = places.filter(county=county)
    if city:
        places = places.filter(city=city)
    if region:
        places = places.filter(region=region)
    if kind:
        places = places.filter(kind=kind)
    if type:
        places = places.filter(type=type)
    if min_score and max_score:
        places = places.filter(average_review_score__gte=min_score, average_review_score__lte=max_score)
    if search:  # Пошук по назві
        places = places.filter(name__icontains=search)

    # Сортування результатів, якщо вказано порядок сортування
    if order_by == 'asc':
        places = places.order_by('average_review_score')
    elif order_by == 'desc':
        places = places.order_by('-average_review_score')

    return render(request, 'main/places.html', {'places': places})

def place_detail(request, place_id):
    place = Place.objects.get(id=place_id)
    form = ReviewForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        review = form.save(commit=False)
        review.place = place
        review.user = request.user  # Запис користувача, який залишив відгук
        review.save()
        return redirect('place-detail', place_id=place.id)
    
    return render(request, 'main/place_detail.html', {'place': place, 'form': form})

def events_page(request):
    events = Event.objects.all()

    # Отримання параметрів фільтрації з URL
    county = request.GET.get('county')
    city = request.GET.get('city')
    region = request.GET.get('region')
    type = request.GET.get('type')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    order_by = request.GET.get('order_by')  # Може бути 'asc' або 'desc'
    search = request.GET.get('search')  # Параметр пошуку по назві

    # Фільтрація за параметрами, якщо вони існують
    if county:
        events = events.filter(place__county=county)
    if city:
        events = events.filter(place__city=city)
    if region:
        events = events.filter(place__region=region)
    if type:
        events = events.filter(type=type)
    if start_date:
        events = events.filter(datetime_start__gte=start_date)
    if end_date:
        events = events.filter(datetime_end__lte=end_date)
    if search:  # Пошук по назві
        events = events.filter(name__icontains=search)

    # Сортування результатів, якщо вказано порядок сортування
    if order_by == 'asc':
        events = events.order_by('datetime_start')
    elif order_by == 'desc':
        events = events.order_by('-datetime_start')

    return render(request, 'main/events.html', {'events': events})

def events_add(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user  # Передача авторизованого користувача до поля owner
            event.save()
            return redirect('event-detail', event_id=event.id)
    else:
        form = EventForm(initial={'owner': request.user})  # Початкове значення для поля owner
        form.fields['owner'].disabled = True  # Робимо поле owner неактивним

    return render(request, 'main/events_add.html', {'form': form})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    # Тут можна передати додаткові дані у шаблон, якщо потрібно
    return render(request, 'main/event_detail.html', {'event': event})