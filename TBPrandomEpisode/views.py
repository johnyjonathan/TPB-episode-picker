from django.shortcuts import render
from .functions import funcs
from .functions import dictionaries

tiles = True
<<<<<<< HEAD


def home(request):
    return render(request, 'tpbrandomepisode/index.html')

def result(request):

    if request.GET.get('wybierz') == 'all':
       season, episode = funcs.random_episode(dictionaries.all_shows)
       name_of_series, filter_seson = funcs.showName(season) 
    elif request.GET.get('wybierz') == 'orginal':
       season, episode = funcs.random_episode(dictionaries.orginal_show)
       name_of_series, filter_seson = funcs.showName(season) 
    return render(request, 'tpbrandomepisode/random.html', {'season': filter_seson, 'name_of_series': name_of_series, 'episode': episode})
=======

def home(request):
        
    if request.method == 'GET':
        return render(request, 'tpbrandomepisode/home.html')
    elif request.POST['wybierz'] == 'all':
        orginal_series = False
        episode = funcs.Episode()
        season, episode = episode.random_episode()
        name_of_series, filter_seson = episode.showName(season)
        return render(request, 'tpbrandomepisode/result.html',{'season': season, 'episode': episode, 'name_of_series': name_of_series, 'filter_seson': filter_seson})
>>>>>>> main

