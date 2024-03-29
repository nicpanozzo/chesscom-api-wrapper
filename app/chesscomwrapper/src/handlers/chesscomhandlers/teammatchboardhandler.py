from typing import Optional
from ..chesscomhandler import ChesscomHandler
from ..errorhandlers.noneerrorhandler import NoneErrorHandler
from ..requesthandlers.singletonrequesthandler import SingletonRequestHandler
from ...models.teammatch.teammatchboardinfo import TeamMatchBoardInfo

class TeamMatchBoardHandlerInterface:
    """An interface to handle the requests to the chess.com API regarding a round"""
    def getInfo(self, url) -> Optional[TeamMatchBoardInfo]:
        """Returns player's monthly archives"""
        pass

class TeamMatchBoardHandler(ChesscomHandler):
    """A class to handle the requests to the chess.com API regarding a round"""
    def __init__(self):
        """Initializes a RoundHandler object"""
        self.errorHandler = NoneErrorHandler()
        self.requestHandler = SingletonRequestHandler()
        pass


    def getInfo(self, url) -> Optional[TeamMatchBoardInfo]:
        """Returns player's monthly archives"""
        response = self.doRequest(url)
        if response is None:
            return None
        boardinfo = TeamMatchBoardInfo(response.json())
        return boardinfo