from game_logic.board import Board
from game_logic.human_player import HumanPlayer


class Referee():
    def __init__(self, board: Board):
        self.board = board
        self.curr_player = None
        self.next_player = None
        
    def set_players(self, player_1: HumanPlayer, player_2: HumanPlayer):
        self.curr_player = player_1
        self.next_player = player_2

    def switch_turns(self):
        self.curr_player, self.next_player = self.next_player, self.curr_player

    def turn_over(self):
        self.board.clear_highlights()
        self.switch_turns()
        #self.game_over()

    def game_winner(self) -> str:
        if self.board.count_piece(1) > self.board.count_piece(0):
            return "White wins!"
        elif self.board.count_piece(0) > self.board.count_piece(1):
            return "Black wins!"
        else:
            return "Tied!"
    
    def game_over(self) -> bool: # returns None so gotta check that
        if self.board.is_board_full():
            return True
        elif self.board.no_valid_moves(self.curr_player.get_player_color()):
            self.switch_turns()
            # if both players have no valid moves to make
            if self.board.no_valid_moves(self.curr_player.get_player_color()):
                return True
        return False