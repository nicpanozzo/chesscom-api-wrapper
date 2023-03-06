from time import sleep
import requests
import threading

# define interface for request handler
class RequestHandler(object):
    """ Interface for RequestHandler """

    def doRequest(self, endpoint, ts=1):
        """Returns a dictionary of a player's info"""
        raise NotImplementedError

# create a singleton class that implements the interface
class SingletonRequestHandler(RequestHandler):
    """ A python singleton """

    class __impl:
        """ Implementation of the singleton interface """

        def spam(self):
            """ Test method, return singleton id """
            return id(self)

    # storage for the instance reference
    __instance = None

    def doRequest(self, endpoint, ts=1):
        """Returns a dictionary of a player's info"""

        # with self.lock:
        if ts > 0:
            print("Sleeping for " + str(ts) + " seconds")
            sleep(ts/1000)
        # print("Calling: " + endpoint)
        response = requests.get(endpoint)
        print(response.status_code)
        return response
        

    def __init__(self):
        """ Create singleton instance """
        # Check whether we already have an instance
        if SingletonRequestHandler.__instance is None:
            # Create and remember instance
            SingletonRequestHandler.__instance = SingletonRequestHandler.__impl()
            SingletonRequestHandler.__instance.lock = threading.Lock()
        print(SingletonRequestHandler.__instance)
        # Store instance reference as the only member in the handle
        self.__dict__['_Singleton__instance'] = SingletonRequestHandler.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)

class ApiManager(object):
    """A class to manage API calls"""

    ENDPOINTBASE = "https://api.chess.com/pub/"
    PLAYER = "player/"
    STATS = "stats/"
    GAMES = "games/"
    GAMES_TO_MOVE = "games/to-move/"
    GAMES_ARCHIVES = "games/archives/"
    GAMES_MONTHLY_ARCHIVES = "games/YEAR/MONTH/"
    PGN = "pgn/"
    CLUBS = "clubs/"
    TOURNAMENTS = "tournaments/"
    requestsQueue = []

    requestHandler: RequestHandler = SingletonRequestHandler()

    def __init__(self):
        """Initializes an ApiManager object"""
        
        pass
    
    def addRequest(self, endpoint, ts):
        """Adds a request to the queue"""

        # self.requestsQueue.append((endpoint, ts))
        # while len(self.requestsQueue) > 0:

        #     for request in self.requestsQueue:
                
        #         if request[0] == endpoint:
        #             sleep(request[1])

        #             return requests.get(request[0])
        #         else:
        #             sleep(request[1])
        #             requests.get(request[0])
        # print("Requesting: " + endpoint)
        response = self.requestHandler.doRequest(endpoint, ts)
        print(response.json())
        return response
        # return aux 

    def doRequest(self, endpoint, ts=1):
        """Returns a dictionary of a player's info"""

        # add request to queue
        response = self.addRequest(self.ENDPOINTBASE + endpoint, ts-1)
        # handle time limit exceeded
        if response.status_code == 429:
            print("Time limit exceeded")
            # riprova e aumenta tempo di attesa
            if ts < 10:
                return self.doRequest(endpoint, ts*2)
            # se l'aumento non funziona, allora errore
            else:
                raise Exception("Time limit exceeded", response.status_code, response.text, endpoint)
            
        elif response.status_code != 200:
            # allora errore
            return response
            raise Exception("Error in API call", response.status_code, response.text, self.ENDPOINTBASE + endpoint)

        return response

    def getPlayerProfile(self, username):
        """Returns a dictionary of a player's info"""
        response = self.doRequest(self.PLAYER + username)
        return response.json()

    def getPlayerStats(self, username):
        """Returns a dictionary of a player's stats"""
        response = self.doRequest(self.PLAYER + username + "/" + self.STATS)
        self.json = response.json()
        
        return response.json()
    
    def getPlayerGames(self, username):
        """Returns a dictionary of a player's games"""
        response = self.doRequest(self.PLAYER + username + "/" + self.GAMES)
        self.json = response.json()
        
        return response.json()