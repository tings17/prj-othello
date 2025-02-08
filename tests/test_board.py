import unittest
from game_logic.board import Board

class TestBoard(unittest.TestCase):
    
    def setUp(self):
        """Set up the board before each test"""
        self.board = Board()

    def test_initial_setup(self):
        # Ensure the initial setup is correct
        white_count = self.board.count_piece(0)
        black_count = self.board.count_piece(1)
        self.assertEqual(white_count, 2)
        self.assertEqual(black_count, 2)

    def test_is_board_full(self):
        # Test that the board is not full initially
        self.assertFalse(self.board.is_board_full())

    def test_count_piece(self):
        self.assertEqual(self.board.count_piece(0)+self.board.count_piece(1), 4)

    def test_no_valid_moves(self):
        # Test that moves are available at the start
        self.assertFalse(self.board.no_valid_moves(0))
        self.assertFalse(self.board.no_valid_moves(1))

    def test_valid_move(self):
        # Test if valid moves are correctly identified
        self.assertTrue(self.board.valid_move(2, 3, 0, False))
        self.assertTrue(self.board.valid_move(4,5,0, False))
        self.assertFalse(self.board.valid_move(3,2,1, False))
        self.assertFalse(self.board.valid_move(5,1,1, False))

if __name__ == "__main__":
    unittest.main()
