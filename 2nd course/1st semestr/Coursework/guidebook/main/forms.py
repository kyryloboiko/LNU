from django import forms
from .models import Event, Review

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['place', 'owner', 'name', 'type', 'description', 'datetime_start', 'datetime_end', 'country', 'region', 'city', 'latitude', 'longitude', 'guests', 'image']
        # Упевніться, що поля відображають усі необхідні поля вашої моделі

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'score']