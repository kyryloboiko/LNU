from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Review
from django.db import models

@receiver(post_save, sender=Review)
def update_average_review_score(sender, instance, **kwargs):
    place = instance.place
    reviews = Review.objects.filter(place=place)
    total_reviews = reviews.count()
    total_score = reviews.aggregate(total=models.Sum('score'))['total']

    place.total_reviews = total_reviews
    place.total_score = total_score or 0
    place.average_review_score = place.total_score / place.total_reviews if place.total_reviews > 0 else 0
    place.save()
