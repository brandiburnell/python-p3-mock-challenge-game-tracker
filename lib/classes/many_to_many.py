class Game:
    def __init__(self, title):
        self.title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) and (hasattr(self, 'title') == False):
                self._title = title
        else:
            raise ValueError("Title must be a non-empty string and cannot be reassigned")


    def results(self):
        pass

    def players(self):
        pass

    def average_score(self, player):
        pass

class Player:
    def __init__(self, username):
        self.username = username

    def results(self):
        pass

    def games_played(self):
        pass

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

class Result:
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score