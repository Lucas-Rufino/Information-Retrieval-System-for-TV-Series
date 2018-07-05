from django.shortcuts import render
import os
import json
from .forms import queryForm
from indexer import processor
from indexer import index
from ranking.ranking import Ranking

_iFile = index.Frequency()
_iFile.load()
_rank = Ranking(_iFile)

def search_page(request):
    genres = ['action', 'adventure', 'animation', 'anime', 'biography', 'comedy', 'crime', 'documentary', 'drama', 'erotic', 'family', 'fantasy', 'fiction', 'gameshow', 'history', 'homeandgarden', 'horror', 'kids', 'movie', 'music', 'musical', 'mystery', 'news', 'politics', 'reality', 'romance', 'scifi', 'soap', 'specialinterest', 'sport', 'superhero', 'suspense', 'talkshow', 'thriller', 'war', 'western']
    return render(request, 'series/search.html', {'genres': genres})

def results_page(request):
    title_query = None
    general_query = None
    cast_query = None
    genre_query = None
    resume_query = None
    rate_query = None

    if request.method == "POST":
        title_query = request.POST.get('title')
        general_query = request.POST.get('general')
        cast_query = request.POST.get('cast')
        genre_query = request.POST.getlist('genre')
        resume_query = request.POST.get('resume')
        rate_query = request.POST.get('rate')
        query = {}
        if title_query != None and title_query != "":
            query['title'] = processor.text(title_query)
        if general_query != None and general_query != "":
            query['all'] = processor.text(general_query)
        if cast_query != None and cast_query != "":
            query['cast'] = processor.text(cast_query)
        if resume_query != None and resume_query != "":
            query['resume'] = processor.text(resume_query)
        if genre_query != None and genre_query != "":
            query['genre'] = genre_query
        if rate_query != None and rate_query != "":
            query['rate'] = processor.number(int(rate_query))
            print(query['rate'])


    data = _iFile.search(query)
    ids_result = _rank.rank(query, data)
    return render(request, 'series/results.html', {'datas': get_response(ids_result)})

def get_data(id):
    path = os.path.abspath(os.path.dirname(__file__))
    filename = str(id)+".json"
    fullpath = os.path.join(path, "../database/"+filename)
    with open(fullpath) as json_data:
        d = json.load(json_data)
        return d

def get_response(ids):
    result = []
    for id in ids:
        data = get_data(id)
        data.update({'id': id})
        result.append(data)
    return result
