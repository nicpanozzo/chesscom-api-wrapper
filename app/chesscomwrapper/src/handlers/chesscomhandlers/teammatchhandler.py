from typing import Optional
from ..chesscomhandler import ChesscomHandler
from ..errorhandlers.noneerrorhandler import NoneErrorHandler
from ..requesthandlers.singletonrequesthandler import SingletonRequestHandler
from ...models.teammatch.teammatchinfo import TeamMatchInfo

class TeamMatchHandlerInterface:
    """An interface to handle the requests to the chess.com API regarding team's matches"""
    def getInfo(self, url) -> Optional[TeamMatchInfo]:
        """Returns player's monthly archives"""
        pass

class TeamMatchHandler(ChesscomHandler):
    """A class to handle the requests to the chess.com API regarding team's matches"""
    def __init__(self):
        """Initializes a RoundHandler object"""
        self.errorHandler = NoneErrorHandler()
        self.requestHandler = SingletonRequestHandler()
        pass


    def getInfo(self, url) -> Optional[TeamMatchInfo]:
        """Returns player's monthly archives"""
        response = self.doRequest(url)
        if response is None:
            return None
        roundinfo = TeamMatchInfo(response.json())
        return roundinfo