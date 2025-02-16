import sys
import os
import pygame


# Add the root directory of your project to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game_logic.computer_player import ComputerPlayer
from game_logic.board import Board
from game_logic.referee import Referee

class GameUI():
    def __init__(self, board: Board, referee: Referee):
        self.board = board
        self.referee = referee
        self.tile_size = 80 # 640 // 8
        pygame.init()
        self.screen = pygame.display.set_mode((self.tile_size * 11, self.tile_size * 8))
        pygame.display.set_caption("OTHELLO")

    def draw_board(self):#, board: Board):
        self.screen.fill((34, 139, 34))
        side_bar = pygame.Rect(self.tile_size * 8, 0, self.tile_size * 3, self.tile_size * 8)
        pygame.draw.rect(self.screen, (110, 98, 98), side_bar)
        for row in range(8):
            for col in range(8):
                x  = col * self.tile_size
                y = row * self.tile_size
                tile = pygame.Rect(x, y, self.tile_size, self.tile_size)
                pygame.draw.rect(self.screen, (0, 0 ,0), tile ,1)

                board_tile = self.board.get_square_at(row, col)

                # highlight moves
                if board_tile.get_piece_color() == "X":
                    pygame.draw.rect(self.screen, (128, 128, 128), tile)

                # draw pieces
                if not board_tile.is_empty():
                    piece_color = (0,0,0) if board_tile.get_piece_color() == 0 else (255, 255, 255)
                    pygame.draw.circle(self.screen, piece_color, tile.center, self.tile_size // 2 - 3)
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                click_row = y // self.tile_size
                click_col = x // self.tile_size
                try:
                    #making a move for the current player
                    self.referee.curr_player.make_move(click_row, click_col)
                    self.board.clear_highlights()
                    self.draw_board()
                except Exception:
                    font = pygame.font.Font(None, 36)
                    text_surface = font.render("Invalid move", True, (255 ,0 ,0))
                    self.screen.blit(text_surface, (self.tile_size * 8.5, self.tile_size * 4))
                    pygame.display.flip()
                else:
                    self.referee.switch_turns()
                    game_over = self.referee.game_over()
                    if game_over:
                        font = pygame.font.Font(None, 36)
                        text_surface = font.render("GAME OVER \n " + self.referee.game_winner(), True, (255 ,0 ,0))
                        self.screen.blit(text_surface, (self.tile_size * 8.5, self.tile_size * 4))
                        pygame.display.flip()
                    else:
                        self.board.highlight_moves(self.referee.curr_player.get_player_color())
                        self.draw_board()
                        #self.handle_events()

    def game_loop(self):
        clock = pygame.time.Clock()
        #initializing the board
        self.board.highlight_moves(self.referee.curr_player.get_player_color())
        self.draw_board()
        while True:
            if isinstance(self.referee.curr_player, ComputerPlayer):
            # Let the computer make its move automatically.
                pygame.time.wait(500)  # Pause a bit so you can see the move.
                self.referee.curr_player.make_move()
                self.board.clear_highlights()
                self.draw_board()

            # Check for game over.
                if self.referee.game_over():
                    font = pygame.font.Font(None, 36)
                    text_surface = font.render("GAME OVER " + self.referee.game_winner(), True, (255, 0, 0))
                    self.screen.blit(text_surface, (self.tile_size * 8.5, self.tile_size * 4))
                    pygame.display.flip()
                    # Optionally, break out of the loop.
                    break

                # Switch turn after computer move.
                self.referee.switch_turns()
                self.board.highlight_moves(self.referee.curr_player.get_player_color())
                self.draw_board()
            else:
                self.handle_events()
            clock.tick(60)