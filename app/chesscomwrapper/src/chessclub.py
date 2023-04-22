from app.chesscomwrapper.src.lazy_decorator import lazy_property
from .models.player.playerclub import PlayerClub
from .models.club.clubmember import ClubMember
from .handlers.chesscomhandlers.clubhandler import ClubHandler


class Club(object):
    def __init__(self, clubname: str, lazy = True) -> None:
        self.id = clubname
        if lazy == False:
            self.profile
            self.members

    def __init__(self, playerclub: PlayerClub, lazy = True) -> None:
        self.id = playerclub
        if lazy == False:
            self.profile
            self.members
        


    @lazy_property
    def profile(self):
        return self._getProfile()
    
    @lazy_property
    def members(self):
        return self._getMembers()
    
    
    def _getMembers(self) -> list[ClubMember]:
        return ClubHandler().getMembers(self.id)
    
    def _getProfile(self):
        return ClubHandler().getProfile(self.id)

