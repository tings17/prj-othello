from game_logic.player import Player
from game_logic.board import Board


class HumanPlayer(Player):
    def __init__(self, player_color: int, board: Board):
        self.player_color = player_color
        self.board = board
    
    def make_move(self, referee):
        print("White's turn" if self.player_color == 1 else "Black's turn")
        self.board.highlight_moves(self.player_color)
        self.board.print_board()
        row, col = self.get_move()
        while True:
            if self.board.valid_move(row, col, self.player_color, True):
                self.board.get_square_at(row, col).add_piece(self.player_color)
                self.board.print_board()
                break
            else:
                print("Invalid move")
                row, col = self.get_move()
        referee.turn_over()

    def get_move(self):
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        return row, col
    
    def get_player_color(self) -> int:
        return self.player_color
        