from game_board import GameBoard
from player import Player

class TickTackToe():
    
    def play(self):
        char_list: list = [GameBoard.O_CHAR,
                           GameBoard.X_CHAR]

        game_board = GameBoard()
        i: int = 0
        player2 = Player()
        while True:
            game_board.display()
            place_ok: bool = False
            mod: int = i % 2
            while place_ok is False:
                print(f"Player{mod+1}, Input number: ", end='')
                if i % 2 == 0:
                    number_str = input().strip()
                    if not number_str.isdigit():
                        continue
                    number: int = int(number_str)
                else:
                    number: int = player2.select_place_number(game_board)
                    print(f"{number}", end='')
                place_ok = game_board.place(number, char_list[mod])
            if game_board.is_win(char_list[mod]):
                game_board.display()
                print(f"Player{mod+1} win!")
                break
            if game_board.is_draw():
                game_board.display()
                print('Drow!')
                break
            i += 1


if __name__ == '__main__':
    tick_tock_toe = TickTackToe()
    tick_tock_toe.play()
    