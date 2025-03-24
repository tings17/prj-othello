from game_logic.board import Board
from game_logic.human_player import HumanPlayer

class Referee():
    def __init__(self, board: Board):
        self.board = board
        self.curr_player = None
        self.next_player = None
        self.skip_count = 0  # Track skipped turns
        
    def set_players(self, player_1, player_2):
        self.curr_player = player_1
        self.next_player = player_2

    def switch_turns(self):
        self.curr_player, self.next_player = self.next_player, self.curr_player
        self.skip_count = 0  # Reset skip counter when turn actually changes

    def turn_over(self):
        self.board.clear_highlights()
        self.switch_turns()

    def game_winner(self) -> str:
        black_count = self.board.count_piece(0)
        white_count = self.board.count_piece(1)
        
        if white_count > black_count:
            return f"White wins! {white_count}-{black_count}"
        elif black_count > white_count:
            return f"Black wins! {black_count}-{white_count}"
        else:
            return f"Tied! {black_count}-{white_count}"
    
    def game_over(self) -> bool:
        # Game is over if board is full
        if self.board.is_board_full():
            return True
            
        # Check if current player has no valid moves
        if self.board.no_valid_moves(self.curr_player.get_player_color()):
            # Switch to next player
            orig_player_color = self.curr_player.get_player_color()
            self.switch_turns()
            
            # Check if next player also has no valid moves
            if self.board.no_valid_moves(self.curr_player.get_player_color()):
                # Both players have no moves, game is over
                return True
            else:
                # Next player has moves, not game over
                # But we'll leave turns switched so next player can move
                self.skip_count += 1
                return False
                
        # Current player has valid moves
        return False
        
    def handle_no_moves(self):
        """Helper method to check if current player has no moves and handle it"""
        if self.board.no_valid_moves(self.curr_player.get_player_color()):
            # Check if both players have no moves (game over)
            orig_color = self.curr_player.get_player_color()
            self.switch_turns()
            if self.board.no_valid_moves(self.curr_player.get_player_color()):
                # Both players have no moves - game is over
                return True
            # Only current player had no moves, turn switched
            return False
        # Current player has moves
        return False
""" from game_logic.board import Board
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
        return False """