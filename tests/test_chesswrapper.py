import random
import threading
from src.club.clubprofile import ClubProfile
from src.chessplayer import ChessPlayer
from src.player.chessplayerstats import ChessPlayerStats
from src.player.playerarchive import PlayerArchive
from src.player.playergames import ChesscomGame
from src.player.chessplayerprofile import ChessPlayerProfile

from src.player.playertournament import PlayerTournament
from src.player.playerclub import PlayerClub

import src.chesswrapper as chesswrapper 
import unittest

class Player(unittest.TestCase):
    def test_player_profile(self):
        """Tests an API call to get a player's info"""

        chess_instance = chesswrapper.ChessWrapper()
        player = chess_instance.getPlayer("nicolapanozzo")
        
        player.getProfile()
        

        "Player should be a ChessPlayer object"
        assert isinstance(player.profile, ChessPlayerProfile ), "Player should be a ChessPlayer object"
        assert player.profile.name == "Nicola Panozzo", "Username should be Nicola Panozzo, not {}".format(player.profile.name)
    
    def test_rate_limit(self):
        """Tests the rate limit"""
        chess_instance = chesswrapper.ChessWrapper()
        player = chess_instance.getPlayer("nicolapanozzo")
        player.getProfile()
        
        
        threadPool = []
        for i in range(0, 100):
            playert = chess_instance.getPlayer("nicolapanozzo{}".format(i*random.randint(1,1000)))
            threadPool.append(threading.Thread(target=playert.getProfile))
        # start threads at the same time
        for thread in threadPool:
            thread.start()
        # wait for all threads to finish
        for thread in threadPool:
            thread.join()

        assert threadPool[60].is_alive() == False, "Thread should be dead"

    def test_player_stats(self):
        """Tests an API call to get a player's stats"""

        chess_instance = chesswrapper.ChessWrapper()
        player = chess_instance.getPlayer("nicolapanozzo")
        player.getStats()
        "Player.stats should be a ChessPlayerStats object"
        assert isinstance(player.stats, ChessPlayerStats ), "Player should be a ChessPlayer object"
        assert player.stats.tactics.highest.rating == 2539, "Games should be 2539, not {}".format(player.stats.tactics.highest.rating)
    
    def test_player_games(self):
        """Tests an API call to get a player's games"""

        chess_instance = chesswrapper.ChessWrapper()
        player = chess_instance.getPlayer("erik")
        player.getPlayerGames()

        "Player.games should be a list of ChesscomGame objects"
        assert isinstance(player.games[0], ChesscomGame), "Game[0] should be a ChesscomGame object"
        # assert player.games[0].pgn.game().headers["Result"] == "*", "Game result should be *, not {}".format(player.games[0].pgn.game().headers["Result"])

    def test_player_games_to_move(self):
        """Tests an API call to get a player's games"""

        chess_instance = chesswrapper.ChessWrapper()
        player = chess_instance.getPlayer("erik")
        player.getPlayerGamesToMove()

        "Player.games should be a list of ChesscomGame objects"
        assert isinstance(player.gamesToMove[0], ChesscomGame),  "Game[0] should be a ChesscomGame object"
        assert len(player.gamesToMove) == 1

    def test_player_archives(self):
        """Tests an API call to get a player's archives"""

        chess_instance = chesswrapper.ChessWrapper()
        player = chess_instance.getPlayer("erik")
        player.getPlayerArchives()

        "Player.archives should be a list of ChesscomGame objects"
        assert isinstance(player.archives[0], PlayerArchive),  "Game[0] should be a ChesscomGame object"
        assert len(player.archives) == 189 , "Archives should be 189, not {}".format(len(player.archives))

    def test_player_archived_games(self):
        """Tests an API call to get a player's archives"""

        chess_instance = chesswrapper.ChessWrapper()
        player = chess_instance.getPlayer("erik")
        player.getPlayerArchives()
        player.archives[0].getGames()

        "Player.archives should be a list of ChesscomGame objects"
        assert isinstance(player.archives[0].games[0], ChesscomGame),  "Archive.games should be a list(ChesscomGame) object"
        assert player.archives[0].games[0].rated == True , "In the first game of the first archive should be rated == True, not {}".format(player.archives[0].games[0].rated)
    
    def test_player_clubs(self):
        """Tests an API call to get a player's clubs"""

        chess_instance = chesswrapper.ChessWrapper()
        player = chess_instance.getPlayer("nicolapanozzo")
        player.getPlayerClubs()
        "Player.archives should be a list of ChesscomGame objects"
        assert isinstance(player.clubs[1], PlayerClub),  "Archive.games should be a list(ChesscomGame) object"
        assert player.clubs[1].name == "Bonobo" , "In the first game of the first archive should be rated == True, not {}".format(player.archives[0].games[0].rated)

    def test_player_tournaments(self):
        """Tests an API call to get a player's tournaments"""

        chess_instance = chesswrapper.ChessWrapper()
        player = chess_instance.getPlayer("nicolapanozzo")
        player.getPlayerTournaments()
        print(player.tournaments[0].tournament.settings.time_class)
        "Player.archives should be a list of ChesscomGame objects"
        assert isinstance(player.tournaments[0], PlayerTournament),  "Archive.games should be a list(ChesscomGame) object"
        assert player.tournaments[0].playerResult.wins == 1 , "In the first game of the first archive should be rated == True, not {}".format(player.archives[0].games[0].rated)

    def test_titled_players(self):
        """Tests an API call to get all the titled players"""

        chess_instance = chesswrapper.ChessWrapper()
        titled_players = chess_instance.getTitledPlayers()
        "Player.archives should be a list of ChesscomGame objects"
        assert isinstance(titled_players[0], ChessPlayer),  "Archive.games should be a list(ChesscomGame) object"
        # assert titled_players[0].name == "Magnus Carlsen" , "In the first game of the first archive should be rated == True, not {}".format(player.archives[0].games[0].rated)

class Club(unittest.TestCase):
    def test_club_info(self):
        """Tests an API call to get a club's info"""

        chess_instance = chesswrapper.ChessWrapper()
        club = chess_instance.getClub("bonobo")
        club.getProfile()
        "Club.info should be a ClubInfo object"
        assert isinstance(club.profile, ClubProfile),  "Club.info should be a ClubInfo object"
        assert club.profile.name == "Bonobo" , "Club name should be Bonobo, not {}".format(club.profile.name)
        assert club.profile.average_daily_rating == 824, "Club average_daily_rating should be 824, not {}".format(club.profile.average_daily_rating)

    def test_club_members(self):
        """Tests an API call to get a club's members"""

        chess_instance = chesswrapper.ChessWrapper()
        club = chess_instance.getClub("bonobo")
        club.getMembers()
        "Club.members should be a list of ChessPlayer objects"
        assert isinstance(club.members[0].player, ChessPlayer),  "Club.members should be a list of ChessPlayer objects"
        assert club.members[0].player.username == "capitanoorsoblu" , "Club member should be capitanoorsoblu, not {}".format(club.members[0].player.username)
