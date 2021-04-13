from django.shortcuts import render
from .functions import funcs

tiles = True
orginal_show = {
    'sezon1': 6 , 
    'sezon2': 7,
    'sezon3': 8,
    'sezon4': 8,
    'sezon5': 10,
    'sezon6': 6,
    'sezon7': 10,
    'sezon8': 10,
    'sezon9': 10,
    'sezon10': 10,
    'sezon11': 10,
    'sezon12': 10,
     }

animated_show = {
    'sezon1': 10,
    'sezon2':10,
}

euro_show = {
    'sezon1': 8,
}

usa_show = {
    'sezon1':8, 
}

shows_names = ['Trailer Park Boys', 'Trailer Park Boys: The Animated Series', 'Trailer Park Boys: Out of the Park: USA', 'Trailer Park Boys: Out of the Park: Europe']

all_shows = list(orginal_show.values()) + list(animated_show.values()) + list(euro_show.values()) + list(usa_show.values())

def home(request):
        
    if request.method == 'GET':
        return render(request, 'tpbrandomepisode/home.html')
    elif request.POST['wybierz'] == 'all':
        orginal_series = False
        season, episode = funcs.random_episode(all_shows)
        name_of_series, filter_seson = funcs.showName(season)
        return render(request, 'tpbrandomepisode/result.html',{'season': season, 'episode': episode, 'name_of_series': name_of_series, 'filter_seson': filter_seson})

