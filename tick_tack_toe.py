from game_board import GameBoard
from player import Player

class TickTackToe():

    O_USER: int = 0
    X_USER: int = 1
    WIN_POINT: int = 1
    DRAW_POINT: int = 0
    LOSE_POINT: int = -1
    
    def play(self):
        char_list: list = [GameBoard.O_CHAR,
                           GameBoard.X_CHAR]
        player2 = Player()
        while True:
            game_board = GameBoard()
            i: int = 0
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
                    if mod == __class__.O_USER:
                        player2.set_q_table(__class__.LOSE_POINT)
                    else:
                        player2.set_q_table(__class__.WIN_POINT)
                    break
                if game_board.is_draw():
                    game_board.display()
                    print('Drow!')
                    player2.set_q_table(__class__.DRAW_POINT)
                    break
                i += 1

if __name__ == '__main__':
    tick_tock_toe = TickTackToe()
    tick_tock_toe.play()
    