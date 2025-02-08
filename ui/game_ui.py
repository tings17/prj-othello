import sys
import os
import pygame


# Add the root directory of your project to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game_logic.board import Board
from game_logic.referee import Referee

class GameUI():
    def __init__(self, board: Board, referee: Referee):
        self.board = board
        self.referee = referee
        self.tile_size = 80 # 640 // 8
        pygame.init()
        self.screen = pygame.display.set_mode((self.tile_size * 8, self.tile_size * 8))
        pygame.display.set_caption("OTHELLO")

    def draw_board(self):#, board: Board):
        self.screen.fill((34, 139, 34))
        for row in range(8):
            for col in range(8):
                x  = col * self.tile_size
                y = row * self.tile_size
                rect = pygame.Rect(x, y, self.tile_size, self.tile_size)
                pygame.draw.rect(self.screen, (0, 0 ,0), rect ,1)

                """
                pygame.draw.rect(self.screen, (0,128,0), (x, y, self.tile_size, self.tile_size))
                pygame.draw.rect(self.screen, (0, 0, 0), (x, y, self.tile_size, self.tile_size), 1)
                """
                board_tile = self.board.get_square_at(row, col)

                # highlight moves
                if board_tile.get_piece_color() == "X":
                    pygame.draw.rect(self.screen, (128, 128, 128), rect)

                # draw pieces
                if not board_tile.is_empty():
                    piece_color = (0,0,0) if board_tile.get_piece_color() == 0 else (255, 255, 255)
                    pygame.draw.circle(self.screen, piece_color, rect.center, self.tile_size // 2 - 3)

                #pygame.display.flip()
                

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
                    self.referee.curr_player.make_move(self.referee, click_row, click_col)
                except Exception:
                    font = pygame.font.Font(None, 36)
                    text_surface = font.render("Invalid move", True, (255 ,0 ,0))
                    self.screen.blit(text_surface,(self.screen .get_width()/2-text_surface .get_width()/2 , self.screen .get_height()-text_surface .get_height()-20))
                    pygame.display.flip()
                    #self.referee.curr_player.make_move(self.referee, click_row, click_col)

    def game_loop(self):
        #board = Board()
        clock = pygame.time.Clock()
        while True:
            self.handle_events()
            self.draw_board()
            self.board.clear_highlights()  # If available; otherwise implement logic to reset "X" states
            self.board.highlight_moves(self.referee.curr_player.get_player_color())
            pygame.display.update()
            clock.tick(60)