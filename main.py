from game_logic.computer_player import ComputerPlayer
from game_logic.board import Board
from game_logic.human_player import HumanPlayer
from game_logic.referee import Referee
from ui.game_ui import GameUI
import cProfile
import pstats


# Instantiate the Board and start the game
def main():
    # Create a new Board object
    board = Board()
    referee = Referee(board)
    #print("Othello Board has been initialized.")
    #player1 = HumanPlayer(0, board) #black
    #player2 = HumanPlayer(1, board) #white
    player1 = ComputerPlayer(0, board, 2) #black
    player2 = ComputerPlayer(1, board, 2) #white
    referee.set_players(player1, player2)
    #print(board.count_piece(0)+board.count_piece(1))
    ui = GameUI(board, referee)
    ui.game_loop()

    # Wrap your game execution in the cProfile:
cProfile.run('main()', 'profile_stats')

# Create a pstats object, for looking at the data:
p = pstats.Stats('profile_stats')

# Sort the output by cumulative time spent in the function
p.sort_stats('cumulative').print_stats(20)
    
    

if __name__ == "__main__":
    main() 