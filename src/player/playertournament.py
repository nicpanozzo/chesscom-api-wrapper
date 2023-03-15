class PlayerTournament(object):

    def __init__(self, data):
        self.playerResult = PlayerResult(data)
        self.tournament = Tournament(data)

class PlayerResult(object):
    def __init__(self, data):
        self.wins = data.get('wins', None)
        self.losses = data.get('losses', None)
        self.draws = data.get('draws', None)
        self.points_awarded = data.get('points_awarded', None)
        self.placement = data.get('placement', None)
        self.status = data.get('status', None)
        self.total_players = data.get('total_players', None)

class Tournament(object):
    def __init__(self, data):
        self.id = data.get('@id', None)
        self.name = data.get('name', None)
        self.url = data.get('url', None)
        self.description = data.get('description', None)
        self.creator = data.get('creator', None)
        self.status = data.get('status', None)
        self.finish_time = data.get('finish_time', None)
        self.settings = TournamentSettings(data)
        self.players = data.get('players', None)
        self.rounds = data.get('rounds', None)
        
class TournamentSettings(object):
    def __init__(self, data) -> None:
        self.type = data.get('type', None)
        self.rules = data.get('rules', None)
        self.is_rated = data.get('is_rated', None)
        self.is_official = data.get('is_official', None)
        self.is_invite_only = data.get('is_invite_only', None)
        self.min_rating = data.get('min_rating', None)
        self.max_rating = data.get('max_rating', None)
        self.initial_group_size = data.get('initial_group_size', None)
        self.user_advance_count = data.get('user_advance_count', None)
        self.use_tiebreak = data.get('use_tiebreak', None)
        self.allow_vacation = data.get('allow_vacation', None)
        self.winner_places = data.get('winner_places', None)
        self.registered_user_count = data.get('registered_user_count', None)
        self.games_per_opponent = data.get('games_per_opponent', None)
        self.total_rounds = data.get('total_rounds', None)
        self.concurrent_games_per_opponent = data.get('concurrent_games_per_opponent', None)
        self.time_class = data.get('time_class', None)
        self.time_control = data.get('time_control', None)