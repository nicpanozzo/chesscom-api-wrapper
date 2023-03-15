import src.requesthandler as requesthandler
import src.errorhandler as errorhandler
from src.errorhandlers.noneerrorhandler import NoneErrorHandler
from src.errorhandlers.raisererrorhandler import RaiserErrorHandler
from src.requesthandlers.singletonrequesthandler import SingletonRequestHandler
class ChesscomHandler(object):
    """ Interface for RequestHandler """
    
    errorHandler: errorhandler.ErrorHandler
    requestHandler: requesthandler.RequestHandler
    
    def doRequest(self, endpoint, ts=1):
        """Returns a dictionary of a player's info"""
        try:
            print("Handling request to: " + endpoint)
            response = self.requestHandler.doRequest(endpoint, ts-1)
            if response.status_code != 200:
                if response.status_code == 301:
                    raise errorhandler.MovedPermanentlyError("Moved Permanently", response.status_code, response.text, endpoint)
                elif response.status_code == 304:
                    raise errorhandler.CacheError("Cache error", response.status_code, response.text, endpoint)
                elif response.status_code == 404:
                    raise errorhandler.MalformedUrlError("Data not available", response.status_code, response.text, endpoint)
                elif response.status_code == 410:
                    raise errorhandler.DataNotAvailableError("Data not available", response.status_code, response.text, endpoint)
                elif response.status_code == 429:
                    raise errorhandler.RateLimitError("Time limit exceeded", response.status_code, response.text, endpoint)
                else:
                    raise errorhandler.OtherError("Other error", response.status_code, response.text, endpoint)
            else:
                return response
        except Exception as e:
            response = self.errorHandler.handle(e)
        
        return response