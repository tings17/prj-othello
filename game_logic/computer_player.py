from game_logic.player import Player
from game_logic.board import Board

class ComputerPlayer(Player):
    def __init__(self, player_color, board: Board, depth: int):
        self.player_color = player_color
        self.board = board
        self.depth = depth

    def minimax(self, board: Board, player_color: int, depth: int, maximizer: bool, alpha, beta):
        opp_color = 1 if player_color == 0 else 0

        if depth == 0: #base case
            return [0,0,board.evaluate_board(player_color)]
        
        all_moves = board.get_all_moves(player_color)

        if not all_moves:
            if not board.get_all_moves(opp_color):
                return [0,0,board.evaluate_board(player_color)]
            else:
                return self.minimax(board, opp_color, depth-1, not maximizer, alpha, beta)
                
        if maximizer:
            best_move = [None, None, float('-inf')]
            for move in all_moves:
                test_board = board.copy_board()
                test_board.valid_move(move[0], move[1], player_color, True)
                test_board.get_square_at(move[0], move[1]).add_piece(player_color)

                score = self.minimax(test_board, opp_color, depth-1, False, alpha, beta)[2]
                if score > best_move[2]:
                    best_move = [move[0], move[1], score]
                
                alpha = max(alpha, score)
                if beta <= alpha:
                    break

            return best_move
        
        else:
            best_move = [None, None, float('inf')]
            for move in all_moves:
                test_board = board.copy_board()
                test_board.valid_move(move[0], move[1], player_color, True)
                test_board.get_square_at(move[0], move[1]).add_piece(player_color)

                score = self.minimax(test_board, opp_color, depth-1, True, alpha, beta)[2]
                if score < best_move[2]:
                    best_move = [move[0], move[1], score]
                
                beta = min(beta, score)
                if beta <= alpha:
                    break

            return best_move
        
    def make_move(self):
        move = self.minimax(self.board, self.player_color, self.depth, True, float('-inf'), float('inf'))
        self.board.valid_move(move[0], move[1], self.player_color, True)
        self.board.get_square_at(move[0], move[1]).add_piece(self.player_color)

    def get_player_color(self) -> int:
        return self.player_color
 