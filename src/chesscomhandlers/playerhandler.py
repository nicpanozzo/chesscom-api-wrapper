from src.errorhandlers.noneerrorhandler import NoneErrorHandler
from src.apimanager import API
import src.chesscomhandler as chesscomhandler
from src.errorhandlers.raisererrorhandler import RaiserErrorHandler
from src.player.chessplayerprofile import ChessPlayerProfile
from src.player.chessplayerstats import ChessPlayerStats
from src.requesthandlers.singletonrequesthandler import SingletonRequestHandler

class PlayerHandler(chesscomhandler.ChesscomHandler):
    """ Handles requests for player data """
    
    def __init__(self):
        """Initializes a PlayerHandler object"""
        self.errorHandler = NoneErrorHandler()
        self.requestHandler = SingletonRequestHandler()
        pass

    def getPlayerProfile(self, username) -> ChessPlayerProfile:
        """Returns a dictionary of a player's info"""
        response = self.doRequest(API.PLAYER_BASE + username)
        if response is None:
            return None
        profile = ChessPlayerProfile(response.json())
        return profile
    
    def getPlayerStats(self, username) -> ChessPlayerStats:
        """Returns a dictionary of a player's stats"""

        response = self.doRequest(API.PLAYER_BASE + username + "/" + API.STATS)

        if response is None:
            return None
        return response.json()
    
    def getPlayerGames(self, username):
        """Returns a dictionary of a player's games"""
        response = self.doRequest(API.PLAYER_BASE + username + "/" + API.GAMES)
        if response is None:
            return None
        return response.json()