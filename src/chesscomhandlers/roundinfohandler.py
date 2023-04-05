from src.errorhandlers.noneerrorhandler import NoneErrorHandler
from src.requesthandlers.singletonrequesthandler import SingletonRequestHandler
from src.chesscomhandler import ChesscomHandler
from src.tournament.tournamentroundgroupinfo import TournamentRoundGroupInfo


class RoundInfoHandler(ChesscomHandler):
    
    def __init__(self):
        """Initializes a RoundHandler object"""
        self.errorHandler = NoneErrorHandler()
        self.requestHandler = SingletonRequestHandler()
        pass


    def getRoundGroupInfo(self, url):
        """Returns player's monthly archives"""
        response = self.doRequest(url)
        if response is None:
            return None
        roundinfo = TournamentRoundGroupInfo(response.json())
        return roundinfo
