from src.chesscomhandlers.playerhandler import PlayerHandler
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
    
    self.profile = PlayerHandler().getPlayerProfile(self.username)
    
  
  def getStats(self):
    """Returns a dictionary of a player's stats"""
    playerStatsJSON = PlayerHandler().getPlayerStats(self.username)
    if playerStatsJSON is not None:
      self.stats = ChessPlayerStats(playerStatsJSON)
    
  def getPlayerGames(self):
    """Returns a dictionary of a player's games"""
    playerGamesJSON = PlayerHandler().getPlayerGames(self.username)
    if playerGamesJSON is not None:
      self.games = list(map(lambda game: ChesscomGame(game), playerGamesJSON['games']))