from game_logic.computer_player import ComputerPlayer
from game_logic.board import Board
from game_logic.human_player import HumanPlayer
from game_logic.referee import Referee
from ui.game_ui import GameUI
import cProfile
import pstats


def main():
    board = Board()
    referee = Referee(board)
    ui = GameUI(board, referee)
    ui.game_loop()

if __name__ == "__main__":
    main() 