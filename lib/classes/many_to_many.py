class Game:

    all = []

    def __init__(self, title):
        self.title = title
        type(self).all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) and (hasattr(self, 'title') == False):
                self._title = title
        else:
            raise Exception("Title must be a non-empty string and cannot be reassigned")

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        all_players = [result.player for result in Result.all if result.game == self]
        print(all_players)
        unique_players = list(set(all_players))
        return unique_players

    def average_score(self, player):
        all_results = self.results()
        player_results = [result for result in all_results if result.player == player]
        total_score = 0
        for result in player_results:
            total_score += result.score
        return total_score / len(player_results)
    
class Player:

    all = []

    def __init__(self, username):
        self.username = username
        type(self).all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) >= 2 and len(username) <= 16:
            self._username = username
        else:
            raise ValueError("Username must be a string between 2 and 16 characters, inclusive.")

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        all_games_played = [result.game for result in Result.all if result.player == self]
        unique_games_played = set(all_games_played)
        unique_games_played_list = list(unique_games_played)
        return unique_games_played_list

    def played_game(self, game):
        games = self.games_played()
        return game in games

    def num_times_played(self, game):
        games = [result.game for result in Result.all if result.player == self]
        counter = 0
        for g in games:
            if g == game:
                counter += 1
        return counter

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)
    
    @property 
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise ValueError("Player must be of type 'Player'")
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise ValueError("Game must be of type 'Game'")
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and not hasattr(self, "score") and 1 <= score <= 5000:
            self._score = score
        else:
            raise ValueError("Score must be an integer between 1 and 5000 and cannot be reassigned")
    
