import chess.pgn
import io

class ChesscomGame:
    def __init__(self, gameJSON):

        self.url = gameJSON["url"]
        self.move_by = gameJSON["move_by"]
        self.pgn = chess.pgn.read_game(io.StringIO(gameJSON["pgn"]))
        self.time_control = gameJSON["time_control"]
        self.last_activity = gameJSON["last_activity"]
        self.rated = gameJSON["rated"]
        self.turn = gameJSON["turn"]
        self.fen = gameJSON["fen"]
        self.start_time = gameJSON["start_time"]
        self.time_class = gameJSON["time_class"]
        self.rules = gameJSON["rules"]
        self.white = gameJSON["white"]
        self.black = gameJSON["black"]
        self.pgnJSON = gameJSON["pgn"]