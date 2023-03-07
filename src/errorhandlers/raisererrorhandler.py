import src.errorhandler as errorhandler
class RaiserErrorHandler(errorhandler.ErrorHandler):
    """ Concrete implementation of ErrorHandler """

    def handle(self, e):
        """How to handle an error"""
        raise e