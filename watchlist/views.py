from django.shortcuts import render
from . import config
import requests

import watchlist

url = 'https://api.themoviedb.org/3/'
api_key = config.api_key

# Create your views here.
def home(request):
    return render(request, 'watchlist/home.html')

def movies(request):
    response = requests.get(f'{url}movie/popular?api_key={api_key}&language=en-US&page=1')
    titles = {'popular':response.json()}
    return render(request, 'watchlist/movies.html', context=titles)

def movie(request, pk):
    response = requests.get(f'{url}movie/{pk}?api_key={api_key}&language=en-US')
    title = response.json()
    return render(request, 'watchlist/movie.html', context=title)
