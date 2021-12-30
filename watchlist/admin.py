from django.contrib import admin

# Register your models here.
from .models import Movie, List

admin.site.register(Movie)
admin.site.register(List)
