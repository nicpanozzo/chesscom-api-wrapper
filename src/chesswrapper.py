import sys



sys.path.append("/Users/nicolapanozzo/unibo/Kaunas Courses/Component Based Software Engineering/chesscom_api_wrapper")

from src.chessclub import Club
from src.chessplayer import ChessPlayer 

class ChessWrapper(object):
  """A class to wrap the chess.com API"""
  
  def __init__(self):
    pass
  


  def getPlayer(self,username):
    """Returns a chess player"""
    player = ChessPlayer(username)

    return player
  
  def getClub(self, clubname):
    """Returns a Club"""
    club = Club(clubname)
    return club
  
  def getTitledPlayers(self):
    """Returns titled players"""
    return list(map(lambda player: ChessPlayer(player), ChessPlayer.getTitledPlayers(self,"GM")))
    

