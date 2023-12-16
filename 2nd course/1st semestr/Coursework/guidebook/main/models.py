from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Place(models.Model):
    name = models.CharField('Назва', max_length=255)
    kind = models.CharField('Вид', max_length=255)
    type = models.CharField('Тип', max_length=255)
    average_review_score = models.FloatField('Середня оцінка відгуків', default=0)
    description = models.TextField('Опис')
    country = models.CharField('Країна', max_length=255)
    region = models.CharField('Регіон, область', max_length=255)
    city = models.CharField('Місто, населений пункт', max_length=255)
    latitude = models.FloatField('Широта', default=0)
    longitude = models.FloatField('Довгота', default=0)
    total_reviews = models.IntegerField('Кількість відгуків', default=0)
    total_score = models.IntegerField('Загальна оцінка', default=0)

    def __str__(self):
        return self.name
    
class User(models.Model):
    name = models.CharField("Ім'я", max_length=255)
    email = models.EmailField('Електронна почта')
    phone_number = models.CharField('Номер телефону', max_length=255)
    date_of_birth = models.DateField('Дата народження')
    gender = models.CharField('Стать', max_length=255)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Назва', max_length=255)
    description = models.TextField('Опис')
    datetime_start = models.DateTimeField('Дата та час початку')
    datetime_end = models.DateTimeField('Дата та час закінчення')
    latitude = models.FloatField('Широта', default=0)
    longitude = models.FloatField('Довгота', default=0)
    guests = models.TextField('Гості')

    def __str__(self):
        return self.name
    
class Review(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField('Відгук')
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        place = self.place
        reviews = Review.objects.filter(place=place)
        total_reviews = reviews.count()
        total_score = reviews.aggregate(total=models.Sum('score'))['total']

        place.total_reviews = total_reviews
        place.total_score = total_score or 0
        place.average_review_score = place.total_score / place.total_reviews if place.total_reviews > 0 else 0
        place.save()

    def __str__(self):
        return self.user + "review"
    
class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField('Дата та час')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user + "attended"