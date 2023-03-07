BASE_URL = "https://api.chess.com/pub/"

class API():
    """A class to manage API calls"""
    # PLAYER API (PLAYER_BASE + username (+ ?))
    PLAYER_BASE = BASE_URL + "player/"
    STATS = "stats/"
    GAMES = "games/"
    GAMES_TO_MOVE = "games/to-move/"
    GAMES_ARCHIVES = "games/archives/"
    GAMES_MONTHLY_ARCHIVES = "games/YEAR/MONTH/"
    PGN = "pgn/"
    CLUBS = "clubs/"
    TOURNAMENTS = "tournaments/"