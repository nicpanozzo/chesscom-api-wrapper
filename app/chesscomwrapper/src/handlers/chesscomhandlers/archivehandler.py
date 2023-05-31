from ...apimanager import API
from ..chesscomhandler import ChesscomHandler
from ..errorhandlers.noneerrorhandler import NoneErrorHandler
from ..requesthandlers.singletonrequesthandler import SingletonRequestHandler
from ...models.player.playergames import ChesscomGame, ChesscomGameArchived

class ArchiveHandlerInterface:
    """An interface to handle the requests to the chess.com API regarding a player's monthly archives"""
    def getGames(self, username, year, month) -> list[ChesscomGame]:
        pass
    
    def getPGN(self, username, year, month) -> str:
        pass

class ArchiveHandler(ChesscomHandler, ArchiveHandlerInterface):
    
    def __init__(self):
        """Initializes a ArchiveHandler object"""
        self.errorHandler = NoneErrorHandler()
        self.requestHandler = SingletonRequestHandler()
        pass


    def getGames(self, username, year, month):
        """Returns player's monthly archives"""
        response = self.doRequest(API.PLAYER_BASE + username + "/" + API.GAMES + year + "/" + month)
        if response is None:
            return None
        games = list(map(lambda game: ChesscomGameArchived(game), response.json()['games']))
        return games
        
    def getPGN(self, username, year, month):
        """Returns player's monthly archives"""
        response = self.doRequest(API.PLAYER_BASE + username + API.GAMES + year + "/" + month + "/" + API.PGN)
        if response is None:
            return None
        pgn = response.data
        return pgn

