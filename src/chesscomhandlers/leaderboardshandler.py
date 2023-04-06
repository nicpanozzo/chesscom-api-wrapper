from src.leaderboards.leaderboardsinfo import LeaderboardsInfo
from src.apimanager import API
from src.errorhandlers.noneerrorhandler import NoneErrorHandler
from src.requesthandlers.singletonrequesthandler import SingletonRequestHandler
from src.chesscomhandler import ChesscomHandler


class LeaderboardsHandler(ChesscomHandler):
    def __init__(self):
        """Initializes a LeaderboardsHandler object"""
        self.errorHandler = NoneErrorHandler()
        self.requestHandler = SingletonRequestHandler()
        pass
    
    def getLeaderboards(self):
        """Returns a leaderboardsInfo object"""
        response = self.doRequest(API.BASE_URL + API.LEADERBOARDS)
        if response is None:
            return None
        leaderboardsInfo = LeaderboardsInfo(response.json())
        return leaderboardsInfo