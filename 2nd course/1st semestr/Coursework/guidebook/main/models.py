from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Place(models.Model):
    name = models.TextField()
    type = models.TextField()
    average_review_score = models.FloatField()
    description = models.TextField()
    country = models.TextField()
    region = models.TextField()
    city = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

class User(models.Model):
    name = models.TextField()
    email = models.EmailField()
    date_of_birth = models.DateField()
    gender = models.TextField()
    phone_number = models.TextField()

class Event(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    guests = models.TextField()

class Review(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
