from django.db import models
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name= 'reviews')
    stars = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
