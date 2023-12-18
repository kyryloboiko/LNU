from . import views
from django.urls import path
from .models import Place, Event, Review
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.places_page, name='home'),
    path('places/', views.places_page, name='places'),
    path('events/', views.events_page, name='events'),
    path('events/add/', views.events_add, name='events_add'),
    path('places/<int:place_id>/', views.place_detail, name='place-detail'),
    path('events/<int:event_id>/', views.event_detail, name='event-detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
