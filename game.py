from random import randint
from player import AI, User
from board import Board, BoardException, BoardWrongShipException


class Game:
    _step = 0
    _has_winner = False
    _directions = ['horizontal', 'vertical']

    def __init__(self, size):
        self.size = size
        self.ai_board = self.random_board()
        self.user_board = self.random_board(False)
        self.ai = AI(self.ai_board, self.user_board)
        self.user = User(self.user_board, self.ai_board)

    def random_board(self, hidden=True):
        board = None
        while board is None:
            board = self.fill_random_board(hidden)
        return board

    def fill_random_board(self, hidden=True):
        tries = 0
        board = Board(hidden, self.size)

        for length in [3, 2, 2, 1, 1, 1, 1]:
            while True:
                tries += 1

                if tries > 3000:
                    return None

                try:
                    x = randint(0, self.size - 1)
                    y = randint(0, self.size - 1)
                    direction = self.random_direction()
                    print(f'{x+1}:{y+1} / {direction} / {length}')
                    board.add_ship(length, x, y, direction)

                    break
                except BoardWrongShipException:
                    pass

        return board

    def random_direction(self):
        idx = randint(0, 1)

        return self._directions[idx]

    @staticmethod
    def greet():
        print("-------------------")
        print("  Let\'s play  ")
        print("-------------------")
        print(" X - horizontal index  ")
        print(" Y - vertical index ")

    def loop(self):
        self.draw_boards()

        while True:
            try:
                current_user = self.user if self._step % 2 == 0 else self.ai

                repeat = current_user.move()

                if not repeat:
                    self._step += 1

                self.draw_boards()

                if not self.user_board.has_live_ships():
                    print('Congrats! You won!')
                    break
                elif not self.ai_board.has_live_ships():
                    print('Sorry! AI won!')
                    break

            except BoardException as exception:
                print(exception)

    def draw_boards(self):
        print("=" * 20)
        print("User board:")
        print(self.user.own_board)
        print("=" * 20)
        print("AI board:")
        print(self.user.enemy_board)

    def start(self):
        self.greet()
        self.loop()
