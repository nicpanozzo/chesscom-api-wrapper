from typing import Optional
from ...chessclub import Club
from ...chessplayer import ChessPlayer
from ...models.country.countryinfo import CountryInfo
from ...apimanager import API
from ..chesscomhandler import ChesscomHandler
from ..errorhandlers.noneerrorhandler import NoneErrorHandler
from ..requesthandlers.singletonrequesthandler import SingletonRequestHandler

class CountryHandlerInterface:
    """An interface to handle the requests to the chess.com API regarding a country"""
    def getInfo(self, code) -> Optional[CountryInfo]:
        """Returns player's monthly archives"""
        pass
    
    def getPlayers(self, code) -> list[ChessPlayer]:
        """Returns country's players"""
        pass
    
    def getClubs(self, code) -> list[Club]:
        """Returns country's clubs"""
        pass

class CountryHandler(ChesscomHandler, CountryHandlerInterface):
    
    def __init__(self):
        """Initializes a RoundHandler object"""
        self.errorHandler = NoneErrorHandler()
        self.requestHandler = SingletonRequestHandler()
        pass


    def getInfo(self, code) -> Optional[CountryInfo]:
        """Returns player's monthly archives"""
        response = self.doRequest(API.BASE_URL + API.COUNTRY + code)
        if response is None:
            return None
        countryinfo = CountryInfo(response.json())
        return countryinfo
    
    def getPlayers(self, code):
        """Returns country's players"""
        response = self.doRequest(API.BASE_URL + API.COUNTRY + code + "/" + API.PLAYERS)
        if response is None:
            return None
        players = [ChessPlayer(player) for player in response.json()['players']]
        return players
    
    def getClubs(self, code):
        """Returns country's clubs"""
        response = self.doRequest(API.BASE_URL + API.COUNTRY + code + "/" + API.CLUBS)
        if response is None:
            return None

        clubs = [Club(club.split("/")[-1]) for club in response.json()['clubs']]
        return clubs
    