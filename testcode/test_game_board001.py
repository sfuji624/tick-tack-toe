import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from game_board import GameBoard

class TestGameBoard(unittest.TestCase):

    #@unittest.skip('test001')
    def test_display001(self):
        game_board = GameBoard()
        game_board.display()

    #@unittest.skip('test002')
    def test_place001(self):
        game_board = GameBoard()
        ok = game_board.place(1, GameBoard.O_CHAR)
        self.assertTrue(ok)
        print('')
        game_board.display()

    #@unittest.skip('test003')
    def test_is_win001(self):
        game_board = GameBoard()
        ok = game_board.place(1, GameBoard.O_CHAR)
        ok = game_board.place(2, GameBoard.O_CHAR)
        ok = game_board.place(3, GameBoard.O_CHAR)
        game_board.display()
        win = game_board.is_win(GameBoard.O_CHAR)
        self.assertTrue(win)

    #@unittest.skip('test004')
    def test_is_win002(self):
        game_board = GameBoard()
        ok = game_board.place(1, GameBoard.O_CHAR)
        ok = game_board.place(2, GameBoard.O_CHAR)
        game_board.display()
        win = game_board.is_win(GameBoard.O_CHAR)
        self.assertFalse(win)

    #@unittest.skip('test005')
    def test_is_win003(self):
        game_board = GameBoard()
        ok = game_board.place(2, GameBoard.O_CHAR)
        ok = game_board.place(5, GameBoard.O_CHAR)
        ok = game_board.place(8, GameBoard.O_CHAR)
        game_board.display()
        win = game_board.is_win(GameBoard.O_CHAR)
        self.assertTrue(win)

    #@unittest.skip('test006')
    def test_is_win004(self):
        game_board = GameBoard()
        ok = game_board.place(1, GameBoard.O_CHAR)
        ok = game_board.place(5, GameBoard.O_CHAR)
        ok = game_board.place(9, GameBoard.O_CHAR)
        game_board.display()
        win = game_board.is_win(GameBoard.O_CHAR)
        self.assertTrue(win)

    #@unittest.skip('test007')
    def test_is_win005(self):
        game_board = GameBoard()
        ok = game_board.place(3, GameBoard.O_CHAR)
        ok = game_board.place(5, GameBoard.O_CHAR)
        ok = game_board.place(7, GameBoard.O_CHAR)
        game_board.display()
        win = game_board.is_win(GameBoard.O_CHAR)
        self.assertTrue(win)

    #@unittest.skip('test008')
    def test_how_many_blank001(self):
        game_board = GameBoard()
        number: int = game_board.how_many_blank()
        self.assertEqual(number, 9)

    #@unittest.skip('test009')
    def test_how_many_blank002(self):
        game_board = GameBoard()
        ok = game_board.place(3, GameBoard.O_CHAR)
        ok = game_board.place(5, GameBoard.O_CHAR)
        ok = game_board.place(7, GameBoard.O_CHAR)
        number: int = game_board.how_many_blank()
        self.assertEqual(number, 6)

if __name__ == "__main__":
    unittest.main()