from django.shortcuts import render
from .functions import funcs
from .functions import dictionaries

tiles = True



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

