from game_logic.player import Player
from game_logic.board import Board


class HumanPlayer(Player):
    def __init__(self, player_color: int, board: Board):
        self.player_color = player_color
        self.board = board
    
    def make_move(self, row: int, col: int):
        #print("White's turn" if self.player_color == 1 else "Black's turn")
        self.board.highlight_moves(self.player_color)
        if self.board.valid_move(row, col, self.player_color, True):
            self.board.get_square_at(row, col).add_piece(self.player_color)
            #referee.turn_over()
        else:
            raise Exception("Invalid Move")
    
    def get_player_color(self) -> int:
        return self.player_color
        