from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(blank=True)
    release_date = models.DateField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    genres = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')