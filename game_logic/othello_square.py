class OthelloSquare:
    def __init__(self):
        self.piece = None
    
    def add_piece(self, color: int):
        self.piece = color
    
    def change_tile(self):
        if self.piece == "X":
            self.piece = None
        else:
            self.piece = "X"
    
    def flip_piece(self):
        if self.piece == 0:
            self.piece = 1
        else:
            self.piece = 0
    
    def get_piece_color(self):
        return self.piece
    
    def is_empty(self) -> bool:
        if self.piece == 1 or self.piece == 0:
            return False
        return True