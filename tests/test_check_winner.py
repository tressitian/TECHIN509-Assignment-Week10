import unittest
from models.board import Board  # Adjust import if the path differs

class TestCheckWinner(unittest.TestCase):
    def test_no_winner(self):
        board = Board()
        board.grid = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertEqual(board.check_winner(), "")

    def test_row_winner(self):
        board = Board()
        board.grid = [
            ['X', 'X', 'X'],
            ['O', ' ', 'O'],
            [' ', 'O', ' ']
        ]
        self.assertEqual(board.check_winner(), "X")

    def test_column_winner(self):
        board = Board()
        board.grid = [
            ['X', 'O', ' '],
            ['X', 'O', ' '],
            ['X', ' ', 'O']
        ]
        self.assertEqual(board.check_winner(), "X")

    def test_diagonal_winner(self):
        board = Board()
        board.grid = [
            ['X', 'O', ' '],
            ['O', 'X', ' '],
            ['O', ' ', 'X']
        ]
        self.assertEqual(board.check_winner(), "X")

    def test_anti_diagonal_winner(self):
        board = Board()
        board.grid = [
            [' ', 'O', 'X'],
            ['O', 'X', ' '],
            ['X', ' ', 'O']
        ]
        self.assertEqual(board.check_winner(), "X")

    def test_empty_board(self):
        board = Board()
        board.grid = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.assertEqual(board.check_winner(), "")

if __name__ == "__main__":
    unittest.main()