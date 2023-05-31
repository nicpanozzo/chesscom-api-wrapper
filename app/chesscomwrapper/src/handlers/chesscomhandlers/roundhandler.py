from ..errorhandlers.noneerrorhandler import NoneErrorHandler
from ..requesthandlers.singletonrequesthandler import SingletonRequestHandler
from ..chesscomhandler import ChesscomHandler
from ...models.tournament.tournamnetroundinfo import TournamentRoundInfo

class RoundHandlerInterface:
    """An interface to handle the requests to the chess.com API regarding a round"""
    def getInfo(self, url):
        """ Returns a TournamentRoundInfo object"""
        pass

class RoundHandler(ChesscomHandler):
    """A class to handle the requests to the chess.com API regarding a round"""
    def __init__(self):
        """Initializes a RoundHandler object"""
        self.errorHandler = NoneErrorHandler()
        self.requestHandler = SingletonRequestHandler()
        pass


    def getInfo(self, url):
        """ Returns a TournamentRoundInfo object"""
        response = self.doRequest(url)
        if response is None:
            return None
        roundinfo = TournamentRoundInfo(response.json())
        return roundinfo

    