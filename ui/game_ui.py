import sys
import os
import pygame


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game_logic.computer_player import ComputerPlayer
from game_logic.human_player import HumanPlayer
from game_logic.board import Board
from game_logic.referee import Referee
class PlayerSelectionMenu:
    def __init__(self, screen):
        self.screen = screen
        self.tile_size = 80
        self.font = pygame.font.Font(None, 32)
        self.title_font = pygame.font.Font(None, 48)
        
        # Player types: 0 = Human, 1 = Easy AI, 2 = Medium AI, 3 = Hard AI
        self.player_types = ["Human", "Easy AI", "Medium AI", "Hard AI"]
        self.black_player_selection = 0  # Default to Human
        self.white_player_selection = 0  # Default to Human
        
        self.black_buttons = []
        self.white_buttons = []
        
        button_width = self.tile_size * 2
        button_height = self.tile_size * 0.6
        
        for i in range(len(self.player_types)):
            button = pygame.Rect(
                self.tile_size * 3, 
                self.tile_size * 2 + (button_height + 10) * i,
                button_width,
                button_height
            )
            self.black_buttons.append(button)
        
        for i in range(len(self.player_types)):
            button = pygame.Rect(
                self.tile_size * 6,
                self.tile_size * 2 + (button_height + 10) * i,
                button_width,
                button_height
            )
            self.white_buttons.append(button)
        
        self.start_button = pygame.Rect(
            self.screen.get_width() // 2 - button_width // 2,
            self.tile_size * 6,
            button_width,
            button_height
        )
    
    def draw(self):
        self.screen.fill((34, 139, 34))
        
        title_text = self.title_font.render("OTHELLO", True, (255, 255, 255))
        title_x = self.screen.get_width() // 2 - title_text.get_width() // 2
        self.screen.blit(title_text, (title_x, self.tile_size * 0.5))
        
        black_text = self.font.render("Black Player", True, (0, 0, 0))
        white_text = self.font.render("White Player", True, (255, 255, 255))
        
        black_text_x = self.tile_size * 3 + self.tile_size - black_text.get_width() // 2
        white_text_x = self.tile_size * 6 + self.tile_size - white_text.get_width() // 2
        
        self.screen.blit(black_text, (black_text_x, self.tile_size * 1.5))
        self.screen.blit(white_text, (white_text_x, self.tile_size * 1.5))
        
        for i, button in enumerate(self.black_buttons):
            color = (100, 100, 100) if i == self.black_player_selection else (200, 200, 200)
            pygame.draw.rect(self.screen, color, button)
            pygame.draw.rect(self.screen, (0, 0, 0), button, 2)
            
            text = self.font.render(self.player_types[i], True, (0, 0, 0))
            text_x = button.x + button.width // 2 - text.get_width() // 2
            text_y = button.y + button.height // 2 - text.get_height() // 2
            self.screen.blit(text, (text_x, text_y))
        
        for i, button in enumerate(self.white_buttons):
            color = (100, 100, 100) if i == self.white_player_selection else (200, 200, 200)
            pygame.draw.rect(self.screen, color, button)
            pygame.draw.rect(self.screen, (0, 0, 0), button, 2)
            
            text = self.font.render(self.player_types[i], True, (0, 0, 0))
            text_x = button.x + button.width // 2 - text.get_width() // 2
            text_y = button.y + button.height // 2 - text.get_height() // 2
            self.screen.blit(text, (text_x, text_y))
        
        pygame.draw.rect(self.screen, (50, 205, 50), self.start_button)
        pygame.draw.rect(self.screen, (0, 0, 0), self.start_button, 2)
        
        start_text = self.font.render("Start Game", True, (0, 0, 0))
        start_text_x = self.start_button.x + self.start_button.width // 2 - start_text.get_width() // 2
        start_text_y = self.start_button.y + self.start_button.height // 2 - start_text.get_height() // 2
        self.screen.blit(start_text, (start_text_x, start_text_y))
        
        pygame.display.flip()
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            
            for i, button in enumerate(self.black_buttons):
                if button.collidepoint(x, y):
                    self.black_player_selection = i
                    return False
            
            for i, button in enumerate(self.white_buttons):
                if button.collidepoint(x, y):
                    self.white_player_selection = i
                    return False
            
            if self.start_button.collidepoint(x, y):
                return True
        
        return False
    
    def get_player_selections(self):
        return self.black_player_selection, self.white_player_selection

class GameUI():
    def __init__(self, board: Board, referee: Referee):
        self.board = board
        self.referee = referee
        self.tile_size = 80
        pygame.init()
        self.screen = pygame.display.set_mode((self.tile_size * 11, self.tile_size * 8))
        pygame.display.set_caption("OTHELLO")

        self.menu = PlayerSelectionMenu(self.screen)
        self.setup_players()

    def setup_players(self):
        clock = pygame.time.Clock()
        menu_active = True
        
        while menu_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if self.menu.handle_event(event):
                    menu_active = False
            
            self.menu.draw()
            clock.tick(60)
        
        black_selection, white_selection = self.menu.get_player_selections()
        
        player1 = self.create_player(0, black_selection)
        player2 = self.create_player(1, white_selection)
        
        print(black_selection)
        print(white_selection)
        self.referee.set_players(player1, player2)
        
        self.black_player_type = "Human" if black_selection == 0 else f"AI (Lvl {black_selection})"
        self.white_player_type = "Human" if white_selection == 0 else f"AI (Lvl {white_selection})"

    def create_player(self, color, player_type):
        if player_type == 0:
            return HumanPlayer(color, self.board)
        else: 
            difficulty = player_type
            return ComputerPlayer(color, self.board, difficulty)
    
    def draw_board(self):
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

                if board_tile.get_piece_color() == "X":
                    pygame.draw.rect(self.screen, (128, 128, 128), tile)

                if not board_tile.is_empty():
                    piece_color = (0,0,0) if board_tile.get_piece_color() == 0 else (255, 255, 255)
                    pygame.draw.circle(self.screen, piece_color, tile.center, self.tile_size // 2 - 3)
        pygame.display.update()

    def game_loop(self):
        clock = pygame.time.Clock()
        game_over_displayed = False
        
        # initialize board
        self.board.highlight_moves(self.referee.curr_player.get_player_color())
        self.draw_board()
        
        # display current player
        self._update_status_display()
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                    
                if event.type == pygame.MOUSEBUTTONDOWN and not isinstance(self.referee.curr_player, ComputerPlayer):
                    x, y = pygame.mouse.get_pos()
                    if x < self.tile_size * 8: 
                        self._handle_player_click(x, y)
            
            if self.referee.game_over():
                if not game_over_displayed:
                    self._display_game_over()
                    game_over_displayed = True
                    pygame.time.wait(3000)
                    running = False
                continue
                
            if isinstance(self.referee.curr_player, ComputerPlayer) and running:
                self._handle_computer_turn()
                
            clock.tick(60)
            
        pygame.quit()
        
    def _update_status_display(self):
        sidebar = pygame.Rect(self.tile_size * 8, 0, self.tile_size * 3, self.tile_size * 8)
        pygame.draw.rect(self.screen, (110, 98, 98), sidebar)
        
        font_size = int(self.tile_size * 0.4)  # Scale font with tile size
        font = pygame.font.Font(None, font_size)
        
        turn_text = "Black's Turn" if self.referee.curr_player.get_player_color() == 0 else "White's Turn"
        text_surface = font.render(turn_text, True, (255, 255, 255))
        
        turn_x = self.tile_size * 8 + (self.tile_size * 3 - text_surface.get_width()) / 2
        self.screen.blit(text_surface, (turn_x, self.tile_size * 1))
        
        black_score = self.board.count_piece(0)
        white_score = self.board.count_piece(1)
        score_text = f"Black: {black_score} | White: {white_score}"
        score_surface = font.render(score_text, True, (255, 255, 255))
        
        score_x = self.tile_size * 8 + (self.tile_size * 3 - score_surface.get_width()) / 2
        self.screen.blit(score_surface, (score_x, self.tile_size * 2))
        
        pygame.display.flip()

    def _handle_player_click(self, x, y):
        click_row = y // self.tile_size
        click_col = x // self.tile_size
        
        try:
            self.referee.curr_player.make_move(click_row, click_col)
            self.board.clear_highlights()
            self.draw_board()
            
            self.referee.switch_turns()
            
            if self.board.no_valid_moves(self.referee.curr_player.get_player_color()) and not self.referee.game_over():
                font = pygame.font.Font(None, 36)
                text_surface = font.render("No valid moves", True, (255, 0, 0))
                self.screen.blit(text_surface, (self.tile_size * 8.5, self.tile_size * 3))
                pygame.display.flip()
                pygame.time.wait(1500)
                
                self.referee.switch_turns()
            
            # Highlight moves for next player
            self.board.highlight_moves(self.referee.curr_player.get_player_color())
            self.draw_board()
            self._update_status_display()
            
        except Exception as e:
            font = pygame.font.Font(None, 36)
            text_surface = font.render("Invalid move", True, (255, 0, 0))
            self.screen.blit(text_surface, (self.tile_size * 8.5, self.tile_size * 3))
            pygame.display.flip()
            pygame.time.wait(1000)
            
    def _handle_computer_turn(self):
        try:
            pygame.time.wait(500)
            
            self.referee.curr_player.make_move()
            self.board.clear_highlights()
            self.draw_board()
            
            self.referee.switch_turns()
            
            if self.board.no_valid_moves(self.referee.curr_player.get_player_color()) and not self.referee.game_over():
                font = pygame.font.Font(None, 36)
                text_surface = font.render("No valid moves", True, (255, 0, 0))
                self.screen.blit(text_surface, (self.tile_size * 8.5, self.tile_size * 3))
                pygame.display.flip()
                pygame.time.wait(1500)
                
                self.referee.switch_turns()
                
                self._handle_computer_turn()
                return
                
            self.board.highlight_moves(self.referee.curr_player.get_player_color())
            self.draw_board()
            self._update_status_display()
            
        except Exception as e:
            print(f"Computer error: {e}")
            
            # computer can't make a move but game isn't over (switch turn)
            if not self.referee.game_over():
                self.referee.switch_turns()
                self.board.highlight_moves(self.referee.curr_player.get_player_color())
                self.draw_board()
                self._update_status_display()
            
    def _display_game_over(self):
        sidebar = pygame.Rect(self.tile_size * 8, 0, self.tile_size * 3, self.tile_size * 8)
        pygame.draw.rect(self.screen, (110, 98, 98), sidebar)
        
        font_large = pygame.font.Font(None, 48)
        font_small = pygame.font.Font(None, 36)
        
        game_over_text = font_large.render("GAME OVER", True, (255, 0, 0))
        game_over_x = self.tile_size * 8 + (self.tile_size * 3 - game_over_text.get_width()) / 2
        self.screen.blit(game_over_text, (game_over_x, self.tile_size * 1))
        
        winner_text = font_small.render(self.referee.game_winner(), True, (255, 255, 255))
        winner_x = self.tile_size * 8 + (self.tile_size * 3 - winner_text.get_width()) / 2
        self.screen.blit(winner_text, (winner_x, self.tile_size * 2))
        
        black_score = self.board.count_piece(0)
        white_score = self.board.count_piece(1)
        
        black_text = font_small.render(f"Black: {black_score}", True, (0, 0, 0))
        black_x = self.tile_size * 8 + (self.tile_size * 3 - black_text.get_width()) / 2
        self.screen.blit(black_text, (black_x, self.tile_size * 3))
        
        white_text = font_small.render(f"White: {white_score}", True, (255, 255, 255))
        white_x = self.tile_size * 8 + (self.tile_size * 3 - white_text.get_width()) / 2
        self.screen.blit(white_text, (white_x, self.tile_size * 4))
        
        pygame.display.flip()