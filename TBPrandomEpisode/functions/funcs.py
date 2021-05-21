import random




def random_episode(show_list):
    if isinstance(show_list, dict):
        values = show_list.values()
        seasons = len(show_list)
        random_season = random.randint(1, seasons)
        episodes = list(values)[random_season-1]
        rand_episode = random.randint(1, episodes)
        return random_season, rand_episode
    elif isinstance(show_list, list):
        seasons = len(show_list)
        random_season = random.randint(1, seasons)
        episodes = show_list[random_season-1]
        rand_episode = random.randint(1, episodes)
        return random_season, rand_episode



def showName (season_number):
    if season_number <= 12:
        name = shows_names[0]
        season = season_number
    elif season_number > 12 and season_number <= 14:
        name = shows_names[1]
        if season_number == 13:
            season = 1
        elif season_number == 14:
            season = 2
    elif season_number == 15:
        name = shows_names[2]
        season = 1
    elif season_number == 16:
        name = shows_names[3]
        season = 1
    return name, season



shows_names = ['Trailer Park Boys: ', 'Trailer Park Boys: The Animated Series', 'Trailer Park Boys: Out of the Park: USA', 'Trailer Park Boys: Out of the Park: Europe']

#all_shows = list(orginal_show.values()) + list(animated_show.values()) + list(euro_show.values()) + list(usa_show.values())

