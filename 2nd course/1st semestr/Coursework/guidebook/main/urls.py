from . import views
from django.urls import path

urlpatterns = [
    path('', views.places, name='home'),
    path('places/', views.places, name='places'),
    path('events/', views.events, name='events')
]
