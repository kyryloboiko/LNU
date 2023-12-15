from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def places(request):  #The places page
    data = {}
    return render(request, 'main/places.html', data)

def events(request):  #The events page
    return render(request, 'main/events.html')