import src.apimanager as apimanager
from src.player.chessplayerstats import ChessPlayerStats
from src.player.chessplayerprofile import ChessPlayerProfile
from src.player.playergames import ChesscomGame
# from chesswrapper.chessplayerstats import ChessPlayerStats
# from chessplayerprofile import ChessPlayerProfile


class ChessPlayer(object):
  """A class to represent a chess.com player"""

  def __init__(self, username):
    """Initializes a ChessPlayer object"""
    
    self.username = username
    # self.getProfile()
    # self.getStats()
    # self.getPlayerGames()
    pass

  def getProfile(self):
    """Returns a dictionary of a player's profile"""
    playerprofileJSON = apimanager.ApiManager().getPlayerProfile(self.username)
    # if playerprofileJSON['status'] == 404:
    #   raise Exception("Player does not exist")
    
    self.profile = ChessPlayerProfile(playerprofileJSON)
  
  def getStats(self):
    """Returns a dictionary of a player's stats"""
    playerStatsJSON = apimanager.ApiManager().getPlayerStats(self.username)

    self.stats = ChessPlayerStats(playerStatsJSON)
    
  def getPlayerGames(self):
    """Returns a dictionary of a player's games"""
    playerGamesJSON = apimanager.ApiManager().getPlayerGames(self.username)
    self.games = list(map(lambda game: ChesscomGame(game), playerGamesJSON['games']))