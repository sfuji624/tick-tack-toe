import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from game_board import GameBoard
from player import Player

class TestPlayer(unittest.TestCase):

    #@unittest.skip('test001')
    def test_select_position_of_blanck001(self):
        player = Player()
        number: int = player.select_position_of_blanck(1, 9)
        print(f"number: {number}")
        if 1 <= number and number <= 9:
            ok = True
        else:
            ok = False
        self.assertTrue(ok)

    #@unittest.skip('test002')
    def test_position_of_blanck_to_place_number001(self):
        game_board = GameBoard()
        player = Player()
        place_number: int = player.position_of_blanck_to_place_number(
            game_board, 9, 9)
        self.assertEqual(place_number, 9)

    #@unittest.skip('test003')
    def test_position_of_blanck_to_place_number002(self):
        game_board = GameBoard()
        ok = game_board.place(7, GameBoard.O_CHAR)
        player = Player()
        place_number: int = player.position_of_blanck_to_place_number(
            game_board, 8, 8)
        self.assertEqual(place_number, 9)

if __name__ == "__main__":
    unittest.main()