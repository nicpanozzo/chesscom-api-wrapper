# from src.player.playerclub import ClubMember, PlayerClub
from src.club.clubprofile import ClubProfile
from src.club.clubmember import ClubMember
from src.apimanager import API
from src.chesscomhandler import ChesscomHandler, NoneErrorHandler, SingletonRequestHandler
from src.player.playergames import ChesscomGame


class ClubHandler(ChesscomHandler):
    
    def __init__(self):
        """Initializes a ArchiveHandler object"""
        self.errorHandler = NoneErrorHandler()
        self.requestHandler = SingletonRequestHandler()
        pass

    
    

    # def getGames(self, username, year, month):
    #     """Returns player's monthly archives"""
    #     response = self.doRequest(API.PLAYER_BASE + username + "/" + API.GAMES + year + "/" + month)
    #     if response is None:
    #         return None
    #     games = list(map(lambda game: ChesscomGame(game), response.json()['games']))
    #     return games
        
    def getMembers(self, clubname) -> list[ClubMember]:
        """Returns player's monthly archives"""
        response = self.doRequest(API.BASE_URL + API.CLUB + clubname + "/" + "members")
        if response is None:
            return None
        members = list(map(lambda mem: ClubMember(mem["username"], mem["joined"]), response.json()['all_time']))
        return members
    
    def getProfile(self, clubname):
        """Returns player's monthly archives"""
        response = self.doRequest(API.BASE_URL + API.CLUB + clubname)
        if response is None:
            return None
        profile = ClubProfile(response.json())
        return profile