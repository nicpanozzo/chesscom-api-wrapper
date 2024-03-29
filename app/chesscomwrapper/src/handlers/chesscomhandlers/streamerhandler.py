from ...apimanager import API
from ...models.streamer.chessstreamerinfo import ChessStreamerInfo
from ..chesscomhandler import ChesscomHandler
from ..errorhandlers.noneerrorhandler import NoneErrorHandler
from ..requesthandlers.singletonrequesthandler import SingletonRequestHandler

class StreamerHandlerInterface:
    """An interface to handle the requests to the chess.com API to get streamers info"""
    def getStreamersInfo(self) -> list[ChessStreamerInfo]:
        """Returns player's monthly archives"""
        pass

class StreamerHandler(ChesscomHandler):
    """ A class to handle the requests to the chess.com API to get streamers info"""
    def __init__(self):
        """Initializes a RoundHandler object"""
        self.errorHandler = NoneErrorHandler()
        self.requestHandler = SingletonRequestHandler()
        pass


    def getStreamersInfo(self) -> list[ChessStreamerInfo]:
        """Returns player's monthly archives"""
        response = self.doRequest(API.BASE_URL + API.STREAMERS)
        if response is None:
            return None
        streamers =  list(map(lambda streamer: ChessStreamerInfo(streamer), response.json()['streamers']))
        return streamers
