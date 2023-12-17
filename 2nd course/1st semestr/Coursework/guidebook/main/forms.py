from django import forms
from .models import Event, Review
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from bootstrap_datepicker_plus.widgets import DatePickerInput


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    date_of_birth = forms.DateField(
        widget=DatePickerInput(format='%Y-%m-%d')
    )
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'date_of_birth', 'gender')

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['place', 'owner', 'name', 'type', 'description', 'datetime_start', 'datetime_end', 'country', 'region', 'city', 'latitude', 'longitude', 'guests', 'image']
        # Упевніться, що поля відображають усі необхідні поля вашої моделі

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'score']