import threading
import src.chesswrapper as chesswrapper 
import unittest

class Player(unittest.TestCase):
    def test_player_profile(self):
        """Tests an API call to get a player's info"""

        chess_instance = chesswrapper.ChessWrapper()
        player = chess_instance.getPlayer("nicolapanozzo")
        player.getProfile()
        
        
        threadPool = []
        for i in range(0, 100):
            playert = chess_instance.getPlayer("nicolapanozzo{}".format(i*100+4))
            threadPool.append(threading.Thread(target=playert.getProfile))
        # start threads at the same time
        for thread in threadPool:
            thread.start()
        # wait for all threads to finish
        for thread in threadPool:
            thread.join()
            
        

        "Player should be a ChessPlayer object"
        assert isinstance(player.profile, chesswrapper.chessplayer.ChessPlayerProfile ), "Player should be a ChessPlayer object"
        assert player.profile.name == "Nicola Panozzo", "Username should be Nicola Panozzo, not {}".format(player.profile.name)
    
    def test_player_stats(self):
        """Tests an API call to get a player's stats"""

        chess_instance = chesswrapper.ChessWrapper()
        player = chess_instance.getPlayer("nicolapanozzo")
        player.getStats()
        "Player.stats should be a ChessPlayerStats object"
        assert isinstance(player.stats, chesswrapper.chessplayer.ChessPlayerStats ), "Player should be a ChessPlayer object"
        assert player.stats.tactics.highest.rating == 2539, "Games should be 2539, not {}".format(player.stats.tactics.highest.rating)
    
    def test_player_games(self):
        """Tests an API call to get a player's games"""

        chess_instance = chesswrapper.ChessWrapper()
        player = chess_instance.getPlayer("erik")
        player.getPlayerGames()

        "Player.games should be a list of ChesscomGame objects"
        assert isinstance(player.games[0], chesswrapper.chessplayer.ChesscomGame), "Player should be a ChessPlayer object"
        assert player.games[0].pgn.game().headers["Result"] == "*", "Game result should be *, not {}".format(player.games[0].pgn.game().headers["Result"])