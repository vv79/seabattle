from random import randint
from board import BoardException, BoardShootOffException
from dot import Dot


class Player:
    def __init__(self, own_board, enemy_board):
        self.own_board = own_board
        self.enemy_board = enemy_board

    def ask(self):
        while True:
            try:
                print("-------------------")
                print("  Your turn, enter:  ")
                print("-------------------")
                x = int(input("X: "))
                y = int(input("Y: "))

                if not x or not y:
                    print('Enter digits!')
                    continue

                if x not in range(0, self.enemy_board.size+1) or y not in range(1, self.enemy_board.size+1):
                    raise BoardShootOffException()

            except Exception as exception:
                print(exception)
                continue

            return Dot(x - 1, y - 1)

    def move(self):
        while True:
            try:
                dot = self.ask()

                return self.enemy_board.shot(dot)

            except BoardException as e:
                print(e)


class AI(Player):
    def ask(self):
        dot = Dot(randint(0, self.enemy_board.size), randint(0, self.enemy_board.size))
        print("-------------------")
        print("  Enemy turn  ")
        print("-------------------")
        print(f'X: {dot.x+1}, Y: {dot.y+1}')

        return dot


class User(Player):
    pass
