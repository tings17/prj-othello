from game_logic.board import Board
from game_logic.human_player import HumanPlayer
from game_logic.referee import Referee
from ui.game_ui import GameUI

# Instantiate the Board and start the game
def main():
    # Create a new Board object
    board = Board()
    referee = Referee(board)
    #print("Othello Board has been initialized.")
    player1 = HumanPlayer(0, board) #black
    player2 = HumanPlayer(1, board) #white
    referee.set_players(player1, player2)
    #print(board.count_piece(0)+board.count_piece(1))
    ui = GameUI(board, referee)
    ui.game_loop()
    
    

if __name__ == "__main__":
    main() 