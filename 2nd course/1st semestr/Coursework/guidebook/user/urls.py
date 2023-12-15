from . import views
from django.urls import path

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('authorization/', views.authorization, name='authorization'),
    path('profile/', views.profile, name='profile')
]
