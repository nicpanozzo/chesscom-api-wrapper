import src.chessplayer as chessplayer 


class ChessWrapper(object):
  """A class to wrap the chess.com API"""
  
  def __init__(self):
    pass
  


  def getPlayer(self,username):
    """Returns a dictionary of a player's info"""
    player = chessplayer.ChessPlayer(username)

    return player

  

