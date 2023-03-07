import src.errorhandler as errorhandler
class NoneErrorHandler(errorhandler.ErrorHandler):
    """ Concrete implementation of ErrorHandler """
    


    def handle(self, e):
        """Handle returning None"""
        if type(e) is errorhandler.RateLimitError:
            print("error: time limit")
        elif e is not None:
            print("error: " + str(e))
        return None
