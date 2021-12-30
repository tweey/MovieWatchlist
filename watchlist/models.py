from typing import Callable
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Movie(models.Model): 
    movie_id = models.IntegerField(primary_key=True)
    upvoted = models.IntegerField()
    downvoted = models.IntegerField()

class List(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    list_id = models.IntegerField()
    name = models.CharField(max_length=50)
    movies = models.ManyToManyField(Movie)

