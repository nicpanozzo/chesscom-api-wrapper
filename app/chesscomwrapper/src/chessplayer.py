from .player.playerarchive import PlayerArchive
from .chesscomhandlers.playerhandler import PlayerHandler
from .player.chessplayerstats import ChessPlayerStats
from .player.chessplayerprofile import ChessPlayerProfile
from .player.playergames import ChesscomGame
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
    """Returns player's stats"""
    self.stats = PlayerHandler().getPlayerStats(self.username)
    
  def getPlayerGames(self):
    """Returns player's games"""
    self.games = PlayerHandler().getPlayerGames(self.username)

  def getPlayerGamesToMove(self):
    """Returns player's games"""
    self.gamesToMove = PlayerHandler().getPlayerGamesToMove(self.username)
  
  def getPlayerArchives(self):
    """Returns player's archives"""
    self.archives: list[PlayerArchive] = PlayerHandler().getPlayerArchives(self.username)
  
  def getPlayerTournaments(self):
    """Returns player's tournaments"""
    self.tournaments = PlayerHandler().getPlayerTournaments(self.username)

  def getPlayerClubs(self):
    """Returns player's clubs"""
    self.clubs = PlayerHandler().getPlayerClubs(self.username)
  
  @staticmethod
  def getTitledPlayers(self, category):
    """Returns titled players"""
    return PlayerHandler().getTitledPlayers(category)
