class Game:

    def __init__(self, title):
        self._title = None
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if self._title is None:
            if isinstance(title, str) and len(title) > 0:
                self._title = title
            else:
                raise Exception
        else:
            raise Exception

    def results(self):
        return [result for result in Result.all if result.game == self and isinstance(result, Result)]

    def players(self):
        return list({result.player for result in Result.all if result.game == self and isinstance(result.player, Player)})

    def average_score(self, player):
        total_score = 0
        count = 0

        for result in Result.all:
            if result.game == self and result.player == player:
                total_score += result.score
                count += 1

        if count == 0:
            return 0
        else:
            return total_score / count


class Player:

    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception

    def results(self):
        return [result for result in Result.all if result.player == self and type(result) is Result]

    def games_played(self):
        return list({result.game for result in Result.all if result.player == self and type(result.game) is Game})

    def played_game(self, game):
        for result in Result.all:
            if result.game == game and result.player == self:
                return True

        return False

    def num_times_played(self, game):
        times_played = 0

        for result in Result.all:
            if result.game == game and result.player == self:
                times_played += 1
        return times_played


class Result:

    all = []

    def __init__(self, player, game, score):
        if isinstance(player, Player):
            self.player = player
        if isinstance(game, Game):
            self.game = game
        self._score = None
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if self._score is None:
            if isinstance(score, int) and 1 <= score <= 5000:
                self._score = score
            else:
                raise Exception
        else:
            raise Exception
