from src.chesscomhandlers.leaderboardshandler import LeaderboardsHandler
from src.leaderboards.leaderboardsinfo import LeaderboardsInfo


class ChessLeaderboards(object):
    def __init__(self, info: LeaderboardsInfo) -> None:
        self.info = info 
        pass

    @staticmethod
    def getLeaderboards(self):
        """Gets all the leaderboards from Chess.com"""
        return ChessLeaderboards(LeaderboardsHandler().getLeaderboards())