from app.chesscomwrapper.src.lazy_decorator import lazy_property
from .handlers.chesscomhandlers.countryhandler import CountryHandler


class ChessCountry(object):
    def __init__(self, abbr, lazy = True) -> None:
        self.code = abbr
        if lazy == False:
            self.info
            self.players
            self.clubs

    @lazy_property
    def info(self):
        return self._getInfo()
    
    @lazy_property
    def players(self):
        return self._getPlayers()
    
    @lazy_property
    def clubs(self):
        return self._getClubs()
    
    def _getInfo(self) -> None:
        return CountryHandler().getInfo(self.code)

    def _getPlayers(self) -> None:
        return CountryHandler().getPlayers(self.code)
    
    def _getClubs(self) -> None:
        return CountryHandler().getClubs(self.code)