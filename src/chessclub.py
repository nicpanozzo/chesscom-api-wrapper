from src.player.playerclub import PlayerClub
from src.club.clubmember import ClubMember
from src.chesscomhandlers.clubhandler import ClubHandler


class Club(object):
    def __init__(self, clubname: str) -> None:
        self.name = clubname
    
    def __init__(self, playerclub: PlayerClub) -> None:
        self.name = playerclub

    def getMembers(self) -> list[ClubMember]:
        self.members = ClubHandler().getMembers(self.name)
    
    def getProfile(self):
        self.profile = ClubHandler().getProfile(self.name)

