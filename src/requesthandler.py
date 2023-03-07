import src.errorhandler as errorhandler

class RequestHandler(object):
    """ Interface for RequestHandler """
    
    errorHandler: errorhandler.ErrorHandler
    
    def doRequest(self, endpoint, ts=0):
        """Returns a dictionary of a player's info"""
        raise NotImplementedError