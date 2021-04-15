from django.shortcuts import render
from .functions import funcs

tiles = True

def home(request):
        
    if request.method == 'GET':
        return render(request, 'tpbrandomepisode/home.html')
    elif request.POST['wybierz'] == 'all':
        orginal_series = False
        episode = funcs.Episode()
        season, episode = episode.random_episode()
        name_of_series, filter_seson = episode.showName(season)
        return render(request, 'tpbrandomepisode/result.html',{'season': season, 'episode': episode, 'name_of_series': name_of_series, 'filter_seson': filter_seson})

