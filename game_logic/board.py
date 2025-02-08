from game_logic.othello_square import OthelloSquare

class Board:
    '''the constructor for the board class'''
    def __init__(self):
        self.board = [[OthelloSquare() for col in range(8)] for row in range(8)]
        self.set_up_board()
        #self.print_board()

    
    def set_up_board(self):
        for row in range(8):
            for col in range(8):
                if (row == 3 and col == 3) or (row == 4 and col == 4):
                    self.board[row][col].add_piece(1)
                elif (row == 3 and col == 4) or (row == 4 and col == 3):
                    self.board[row][col].add_piece(0)

    def get_square_at(self, row: int, col: int) -> OthelloSquare:
        return self.board[row][col]
    
    def check_one_dir(self, row: int, col: int, row_dir: int, col_dir: int, player_color: int, seen_opp: bool) -> bool:
        """
        checks whether there will be a sandwich in the specified direction from the square we want to place a piece on
        this square needs to be:
        1. not out of bounds
        2. not occupied
        3. an opponent's piece has been found and the square adjacent to that opp is the player's color
        use of recursion to keep checking the direction
        """
        adj_row = row + row_dir
        adj_col = col + col_dir

    
        # check that the adjacent square in that direction is NOT empty and not out of bounds; otherwise, return false
        if not (0 <= adj_row < 8 and 0 <= adj_col < 8):
            return False
        if self.board[adj_row][adj_col].is_empty():
            return False
        # if the adjacent is an opp, we have to check the next adjacent square to that opp 
        elif self.board[adj_row][adj_col].get_piece_color() != player_color:
            return self.check_one_dir(adj_row, adj_col, row_dir, col_dir, player_color, True)
        # if adjacent is same color and we saw the opponent already
        elif self.board[adj_row][adj_col].get_piece_color() == player_color and seen_opp == True:
            return True
        
    def valid_move(self, row: int, col: int, player_color: int, flip: bool) -> bool:
        """
        checks whether the move (placing a square there) is valid not just in one direction but any of the 8 directions
        if even one direction valid, then we return true. If no directions are available, we return false
        we can check directions by offsetting row & col by 1, there's a total combination of 8 directions where there's three
        possibilities of offsets (-1,0,1) because 3^2=9 but one of the 9 is not moving anywhere in a direction (0&0)
        """
        if  (0 <= row < 8 and 0 <= col < 8) and self.board[row][col].is_empty():
            counter = 0
            for row_offset in range(-1, 2, 1):
                for col_offset in range(-1,2,1):
                    if self.check_one_dir(row, col, row_offset, col_offset, player_color, False):
                        if flip is False:
                            return True
                        else:
                            row_flip = row + row_offset
                            col_flip = col + col_offset
                            while self.board[row_flip][col_flip].get_piece_color() != player_color:
                                self.board[row_flip][col_flip].flip_piece()
                                row_flip += row_offset
                                col_flip += col_offset
                            counter += 1
            return counter > 0
        return False
    
    def no_valid_moves(self, player_color: int) -> bool:
        """
        returns true if all squares are not valid to place a piece on
        returns false otherwise (a valid move does exist somewhere on the board
        the difference for this method compared to valid_move is valid_move checks whether placing 
        a piece on a specific square is valid or not
        while this method checks just in general all 64 squares in the board
        """
        #valid_count = 0
        for row in range(8):
            for col in range(8):
                if self.valid_move(row, col, player_color, False):
                    return False
        return True
    
    def is_board_full(self) -> bool:
        for row in range(8):
            for col in range(8):
                if self.board[row][col].is_empty():
                    return False
        return True
    
    def count_piece(self, player_color: int) -> int:
        counter = 0
        for row in range(8):
            for col in range(8):
                if self.board[row][col].get_piece_color() == player_color:
                    counter += 1
        return counter
    
    def highlight_moves(self, player_color):
        for row in range(8):
            for col in range(8):
                if self.valid_move(row, col, player_color, False):
                    print(f"Valid move at: ({row}, {col})")
                    self.board[row][col].change_tile()
    
    def clear_highlights(self):
        for row in range(8):
            for col in range(8):
                if self.board[row][col].get_piece_color() == "X":
                    self.board[row][col].change_tile()
        
    def print_board(self):
        for row in self.board:
            row_repr = []
            for square in row:
                piece = square.get_piece_color()
                # Represent empty squares by "."
                row_repr.append(str(piece) if piece is not None else ".")
            print(" ".join(row_repr))
