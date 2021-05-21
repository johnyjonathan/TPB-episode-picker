import random


class Episode:
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


    def random_episode(self):
        if isinstance(self.show_list, dict):
            self.values = self.show_list.values()
            self.seasons = len(self.show_list)
            self.random_season = random.randint(1, self.seasons)
            self.episodes = list(self.values)[self.random_season-1]
            self.rand_episode = random.randint(1, self.episodes)
            return self.random_season, self.rand_episode
        elif isinstance(self.show_list, list):
            self.seasons = len(self.show_list)
            self.random_season = random.randint(1, self.seasons)
            self.episodes = self.show_list[self.random_season-1]
            self.rand_episode = random.randint(1, self.episodes)
            return self.random_season, self.rand_episode



def showName (self):
    if self.season_number <= 12:
        self.name = self.shows_names[0]
        self.season = self.season_number
    elif self.season_number > 12 and self.season_number <= 14:
        self.name = self.shows_names[1]
        if self.season_number == 13:
            self.season = 1
        elif self.season_number == 14:
            self.season = 2
    elif self.season_number == 15:
        self.name = self.shows_names[2]
        self.season = 1
    elif self.season_number == 16:
        self.name = self.shows_names[3]
        self.season = 1
    return self.name, self.season



<<<<<<< HEAD
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

=======
>>>>>>> main

