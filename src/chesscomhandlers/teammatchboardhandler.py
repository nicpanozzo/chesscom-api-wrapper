from src.chesscomhandler import ChesscomHandler
from src.errorhandlers.noneerrorhandler import NoneErrorHandler
from src.requesthandlers.singletonrequesthandler import SingletonRequestHandler
from src.teammatch.teammatchboardinfo import TeamMatchBoardInfo


class TeamMatchBoardHandler(ChesscomHandler):
    
    def __init__(self):
        """Initializes a RoundHandler object"""
        self.errorHandler = NoneErrorHandler()
        self.requestHandler = SingletonRequestHandler()
        pass


    def getInfo(self, url):
        """Returns player's monthly archives"""
        response = self.doRequest(url)
        if response is None:
            return None
        boardinfo = TeamMatchBoardInfo(response.json())
        return boardinfo