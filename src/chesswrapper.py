import sys






sys.path.append("/Users/nicolapanozzo/unibo/Kaunas Courses/Component Based Software Engineering/chesscom_api_wrapper")

from src.chessclub import Club
from src.chessplayer import ChessPlayer 
from src.chesstournament import Tournament
from src.chessteammatch import TeamMatch
from src.chesscountry import ChessCountry
from src.dailypuzzle import Puzzle, PuzzleFactory
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
  
  def getTournament(self, tournamentId):
    """Returns a tournament"""
    tournament = Tournament(tournamentId)
    return tournament
  
  def getTeamMatch(self, matchUrl):
    """Returns a team match"""
    teamMatch = TeamMatch(matchUrl)
    return teamMatch
  
  def getTitledPlayers(self):
    """Returns titled players"""
    return list(map(lambda player: ChessPlayer(player), ChessPlayer.getTitledPlayers(self,"GM")))
    
  def getCountry(self, countryCode):
    """Returns a country"""
    return ChessCountry(countryCode)
  
  def getDailyPuzzle(self):
    """Returns the daily puzzle"""
    return PuzzleFactory().getDaily()
  
  def getRandomPuzzle(self):
    """Returns a random puzzle"""
    return PuzzleFactory().getRandomPuzzle()

