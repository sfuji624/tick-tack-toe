import traceback
import pandas as pd

class GameBoard:
    #ROW_NUMBER = 3
    #COLUMN_NUMBER = 3
    HORIZONTAL_LINES = '---'
    VERTICAL_LINES = '|'
    INTERSECTION = '+'
    O_CHAR = 'o'
    X_CHAR = 'x'

    def __init__(self):
        self.disc_map = pd.DataFrame({0: ['1', '4', '7'],
                                      1: ['2', '5', '8'],
                                      2: ['3', '6', '9']},
                                      index=[0, 1, 2]) # ゲームに利用する盤面

    def display_horizontal_line(self):
        print(__class__.INTERSECTION, end='')
        for column in range(self.disc_map.shape[1]):
            print(__class__.HORIZONTAL_LINES,
                      end=__class__.INTERSECTION)
        print('')
        
    def display(self):
        print('')
        self.display_horizontal_line()
        i = 0
        for row in range(self.disc_map.shape[0]):
            print(__class__.VERTICAL_LINES, end='')
            for column in range(self.disc_map.shape[1]):
                print(f" {self.disc_map.at[row, column]} ", end=__class__.VERTICAL_LINES)
                i += 1
            print('')
            self.display_horizontal_line()

    def place(self, number: int, o_x: str) -> bool:
        if not (1 <= number and number <= self.disc_map.size):
            return False
        if o_x != __class__.O_CHAR and o_x != __class__.X_CHAR:
            return False
        try:
            #print(f"number: {number}")
            if 1 <= number and number <= self.disc_map.size:
                row: int = int((number - 1) / self.disc_map.shape[0])
                column: int = (number - 1) % self.disc_map.shape[0]
                if self.is_blanck(number):
                    self.disc_map.at[row, column] = o_x
                    return True
            return False
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return False
        
    def is_win(self, disc_char) -> bool:
        if disc_char != __class__.O_CHAR and disc_char != __class__.X_CHAR:
            return False
        
        # 横並び確認
        for row in range(self.disc_map.shape[0]):
            for column in range(self.disc_map.shape[1]):
                if self.disc_map.at[row, column] != disc_char:
                    break
            else:
                return True

        # 縦並び確認
        for column in range(self.disc_map.shape[1]):
            for row in range(self.disc_map.shape[0]):
                if self.disc_map.at[row, column] != disc_char:
                    break
            else:
                return True

        # 斜め確認
        if self.disc_map.at[0, 0] == disc_char and \
            self.disc_map.at[1, 1] == disc_char and \
            self.disc_map.at[2, 2] == disc_char:
                return True
        
        if self.disc_map.at[0, 2] == disc_char and \
            self.disc_map.at[1, 1] == disc_char and \
            self.disc_map.at[2, 0] == disc_char:
                return True
        return False
    
    def is_draw(self):
        for number in range(self.disc_map.size):
            if self.is_blanck(number + 1):
                return False
        return True
    
    def how_many_blank(self):
        blank_number: int = 0
        for number in range(self.disc_map.size):
            if self.is_blanck(number + 1):
                blank_number += 1
        return blank_number
    
    def is_blanck(self, number: int) -> bool:
        if not (1 <= number and number <= self.disc_map.size):
            raise IndexError
        row: int = int((number - 1) / self.disc_map.shape[0])
        column: int = (number - 1) % self.disc_map.shape[0]
        disc: str = self.disc_map.at[row, column]
        if disc.isdigit():
            return True
        else:
            return False
        

            





