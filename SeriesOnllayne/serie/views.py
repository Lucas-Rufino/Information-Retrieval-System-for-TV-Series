from django.shortcuts import render
import os
import json

# Create your views here.
def search_page(request):
    genres = ['action', 'adventure', 'animation', 'anime', 'biography', 'comedy', 'crime', 'documentary', 'drama', 'erotic', 'family', 'fantasy', 'fiction', 'gameshow', 'history', 'homeandgarden', 'horror', 'kids', 'movie', 'music', 'musical', 'mystery', 'news', 'politics', 'reality', 'romance', 'scifi', 'soap', 'specialinterest', 'sport', 'superhero', 'suspense', 'talkshow', 'thriller', 'war', 'western']
    return render(request, 'series/search.html', {'genres': genres})
def results_page(request):
    return render(request, 'series/results.html', {'data': get_data(1)})
def search_query(request):
    title_query = None
    general_query = None
    cast_query = None
    genre_query = None
    resume_query = None

    if request.method == "GET":
        title_query = request.GET.get('title_input', None)
        general_query = request.GET.get('general_input', None)
        cast_query = request.GET.get('cast_input', None)
        resume_query = request.GET.get('resume_input', None)
     
        
def get_data(id):
    path = "data"
    filename = id
    fullpath = os.path.join(path, filename)
    with open(fullpath) as json_data:
        d = json.load(json_data)
        return d



