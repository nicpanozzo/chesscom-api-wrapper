from typing import Optional

from .models.player.titledcategory import TitledCategory

from .models.player.playerclub import PlayerClub

from .models.player.playertournament import PlayerTournaments
from .lazy_decorator import lazy_property
from .playerarchive import PlayerArchive
from .handlers.chesscomhandlers.playerhandler import PlayerHandler
from .models.player.chessplayerstats import ChessPlayerStats
from .models.player.chessplayerprofile import ChessPlayerProfile
from .models.player.playergames import ChesscomGame
# from chesswrapper.chessplayerstats import ChessPlayerStats
# from chessplayerprofile import ChessPlayerProfile


    


class ChessPlayer(object):
  """A class to represent a chess.com player"""

  def __init__(self, username, lazy=True):
    """Initializes a ChessPlayer object"""
    
    self.username = username
    if lazy == False:
      self.profile
      self.stats
      self.games
      self.gamesToMove
      self.tournaments
      self.clubs
    pass
  

  @lazy_property
  def profile(self):
    return self.getProfile()

  @lazy_property
  def stats(self):
    return self.getStats()

  @lazy_property
  def games(self):
    return self.getPlayerGames()

  @lazy_property
  def gamesToMove(self):
    return self.getPlayerGamesToMove()

  @lazy_property
  def tournaments(self):
    return self.getPlayerTournaments()

  @lazy_property
  def clubs(self):
    return self.getPlayerClubs() 


  

  def getProfile(self) -> Optional[ChessPlayerProfile]:
    """Returns a dictionary of a player's profile"""
    
    return PlayerHandler().getPlayerProfile(self.username)
    
  
  def getStats(self) -> Optional[ChessPlayerStats]:
    """Returns player's stats"""
    return PlayerHandler().getPlayerStats(self.username)
    
  def getPlayerGames(self) -> Optional[list[ChesscomGame]]:
    """Returns player's games"""
    return PlayerHandler().getPlayerGames(self.username)

  def getPlayerGamesToMove(self) -> Optional[list[ChesscomGame]]:
    """Returns player's games"""
    return PlayerHandler().getPlayerGamesToMove(self.username)
  
  def getPlayerArchives(self) -> Optional[list[PlayerArchive]]:
    """Returns player's archives"""
    return PlayerHandler().getPlayerArchives(self.username)
  
  def getPlayerTournaments(self) -> Optional[PlayerTournaments]:
    """Returns player's tournaments"""
    return PlayerHandler().getPlayerTournaments(self.username)

  def getPlayerClubs(self) -> Optional[list[PlayerClub]]:
    """Returns player's clubs"""
    return PlayerHandler().getPlayerClubs(self.username)
  
  @staticmethod
  def getTitledPlayers(self, category: TitledCategory):
    """Returns titled players"""
    return list(map(lambda player: ChessPlayer(player),PlayerHandler().getTitledPlayers(category)))
