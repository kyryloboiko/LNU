from . import views
from django.urls import path

urlpatterns = [
    path('registration/', views.registration),
    path('authorization/', views.authorization),
    path('profile/', views.profile)
]
