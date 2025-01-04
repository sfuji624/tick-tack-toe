import pandas as pd
import random
from typing import Tuple

from game_board import GameBoard

class Player:
    def __init__(self):
        pass

    def select_position_of_blanck(self, min: int, max: int) -> int:
        number: int = random.randint(min, max)
        return number
    
    def select_place_number(self, game_boad: GameBoard) -> int:
        blank_number: int = game_boad.how_many_blank()
        position_of_blanck: int = self.select_position_of_blanck(1, blank_number)
        place_number: int = self.position_of_blanck_to_place_number(
                                    game_boad, blank_number, position_of_blanck)
        return place_number


    def position_of_blanck_to_place_number(self, game_boad: GameBoard, 
                            blank_number: int, position_of_blanck: int) ->  int:
        counter: int = 0
        place_number = 1
        while counter < blank_number:
            if game_boad.is_blanck(place_number):
                counter += 1
                if counter == position_of_blanck:
                    return place_number
            place_number += 1
        return 0


