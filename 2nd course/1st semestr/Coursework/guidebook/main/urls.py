from . import views
from django.urls import path
from .models import Attendance, Place, Event, Review
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.places, name='home'),
    path('places/', views.places, name='places'),
    path('events/', views.events, name='events'),
    path('places/<int:place_id>/', views.place_detail, name='place-detail'),
    path('events/<int:event_id>/', views.event_detail, name='event-detail')
]
