from dot import Dot


class BoardException(Exception):
    pass


class BoardShootOffException(BoardException):
    def __str__(self):
        return "You shot off the board."


class BoardAlreadyShottedException(BoardException):
    def __str__(self):
        return "You've already shot here."


class BoardWrongShipException(BoardException):
    pass


class Board:
    def __init__(self, hidden=True, size=6):
        self.hidden = hidden
        self.size = size
        self.ships = []
        self.busy = []
        self.fields = [["O"] * size for _ in range(size)]

    def reset(self):
        self.busy = []

    def add_ship(self, ship):
        for dot in ship.dots:
            if self.out(dot) or dot in self.busy:
                raise BoardWrongShipException()

        for dot in ship.dots:
            self.fields[dot.x][dot.y] = "■"
            self.busy.append(dot)

        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, show=False):
        contour = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for dot in ship.dots:
            for x, y in contour:
                contour_dot = Dot(dot.x + x, dot.y + y)
                if not self.out(contour_dot) and contour_dot not in self.busy:
                    if show:
                        self.fields[contour_dot.x][contour_dot.y] = "."

                    self.busy.append(contour_dot)

    def __str__(self):
        string = "  | " + " | ".join(str(i + 1) for i in range(self.size))

        for i, row in enumerate(self.fields):
            string += f"\n{i + 1} | " + " | ".join(row)

        if self.hidden:
            string = string.replace("■", "O")

        return string

    def out(self, dot):
        return dot.x >= self.size or dot.x < 0 or dot.y >= self.size or dot.y < 0

    def shot(self, dot):
        if dot in self.busy:
            raise BoardAlreadyShottedException()

        if self.out(dot):
            raise BoardShootOffException()

        self.busy.append(dot)

        for ship in self.ships:
            if ship.hit(dot):
                self.fields[dot.x][dot.y] = "X"
                if ship.destroyed():
                    print("The ship is destroyed!")
                    self.contour(ship, True)
                    return False
                else:
                    print("The ship is hit!")
                    return True

        self.fields[dot.x][dot.y] = "."
        print("Miss!")

        return False

    @property
    def live_ships(self):
        live_ships = []

        for ship in self.ships:
            if not ship.destroyed():
                live_ships.append(ship)

        return live_ships

    def has_live_ships(self):
        return True if len(self.live_ships) > 0 else False
