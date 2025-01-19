import math
import numpy as np
import pandas as pd
import random
from typing import Tuple

from game_board import GameBoard

class Player:
    # action 0 ～ 8 ... place_number - 1
    # status 0 ～ 4 ** 9 - 1
    # place_number 1 ～ 9

    def __init__(self):
        self.this_game_record = dict()
        self.q_table = pd.DataFrame()
        base: int = GameBoard.BASE
        max_place_number: int = GameBoard.MAX_PLACE_NUMBER
        self.q_table = pd.DataFrame(np.zeros((base ** (max_place_number),
                                              max_place_number)))
        self.turn: int = 0

    def select_position_of_blanck(self, min: int, max: int) -> int:
        number: int = random.randint(min, max)
        return number
    
    def select_place_number(self, game_boad: GameBoard) -> int:
        before_status: int = game_boad.get_status()
        blank_number: int = game_boad.how_many_blank()
        position_of_blanck: int = self.select_position_of_blanck(1, blank_number)
        place_number: int = self.position_of_blanck_to_place_number(
                                    game_boad, blank_number, position_of_blanck)
        self.record(before_status, place_number - 1)
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
    
    def record(self, status:int, action: int):
        row: int = self.turn
        self.this_game_record[status] = action
        print('')
        print(f"status: {status}")
        print('this_game_record: ')
        print(f"{self.this_game_record}")
        self.turn += 1

    def set_q_table(self, point: int):
        for status in self.this_game_record:
            action : int = self.this_game_record[status]
            print(f"status: {status}, action: {action}")
            if math.isnan(self.q_table.at[status, action - 1]):
                self.q_table.at[status, action - 1] = point
            else:
                self.q_table.at[status, action - 1] += point
        self.trun = 0
        self.this_game_record = dict()
        print(f"q_table: {self.q_table}")
