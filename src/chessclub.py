from src.player.playerclub import PlayerClub
from src.club.clubmember import ClubMember
from src.chesscomhandlers.clubhandler import ClubHandler


class Club(object):
    def __init__(self, clubname: str) -> None:
        self.id = clubname
    
    def __init__(self, playerclub: PlayerClub) -> None:
        self.id = playerclub

    def getMembers(self) -> list[ClubMember]:
        self.members = ClubHandler().getMembers(self.id)
    
    def getProfile(self):
        self.profile = ClubHandler().getProfile(self.id)

