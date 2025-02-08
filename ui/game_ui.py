import sys
import os
import pygame

# Add the root directory of your project to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game_logic.board import Board


pygame.init()

window = pygame.display.set_mode((640, 640))

def draw_board(board: Board):
    tile_size = 640 // 8
    for row in range(8):
        for col in range(8):
            x  = col * tile_size
            y = row * tile_size
            pygame.draw.rect(window, (0,128,0), (x, y, tile_size, tile_size))
            pygame.draw.rect(window, (0, 0, 0), (x, y, tile_size, tile_size), 1)
            board_tile = board.get_square_at(row, col)
            if not board_tile.is_empty():
                piece_color = (0,0,0) if board_tile.get_piece_color() == 0 else (255, 255, 255)
                pygame.draw.circle(window, piece_color, (col * tile_size + 40, row * tile_size + 40), 30)

def mouse_click():
    x, y = pygame.mouse.get_pos()
    click_row = x / 80
    click_col = y / 80
    return click_row, click_col

def player_input(click, board: Board):
    if click.type == pygame.MOUSEBUTTONDOWN:
        row, col = mouse_click()
        if board.

def highlight_move(board, player_color):
    for row in range(8):
        for col in range(8):
            if board.

def game_loop():
    board = Board()
    running = True
    while running:
        draw_board(board)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

game_loop()