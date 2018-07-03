from django.shortcuts import render

# Create your views here.
def search_page(request):
    genres = ['action', 'adventure', 'animation', 'anime', 'biography', 'comedy', 'crime', 'documentary', 'drama', 'erotic', 'family', 'fantasy', 'fiction', 'gameshow', 'history', 'homeandgarden', 'horror', 'kids', 'movie', 'music', 'musical', 'mystery', 'news', 'politics', 'reality', 'romance', 'scifi', 'soap', 'specialinterest', 'sport', 'superhero', 'suspense', 'talkshow', 'thriller', 'war', 'western']
    return render(request, 'series/search.html', {'genres': genres})

