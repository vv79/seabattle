from ship import Ship
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
        self.ships_dots = []
        self.contour_dots = []
        self.shotted_dots = []
        self.fields = [["O"] * size for _ in range(size)]

    def add_ship(self, length, x, y, direction):
        ship = Ship(length, x, y, direction)

        for dot in ship.dots:
            if self.out(dot) or dot in self.ships_dots or dot in self.contour_dots:
                raise BoardWrongShipException()

        for dot in ship.dots:
            self.fields[dot.x][dot.y] = "■"
            self.ships_dots.append(dot)

        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, replace = False):
        for contour_dot in ship.contour_dots:
            if not (self.out(contour_dot)) and contour_dot not in self.ships_dots:
                if replace:
                    self.fields[contour_dot.x][contour_dot.y] = "."

                self.contour_dots.append(contour_dot)

    def __str__(self):
        string = "  | " + " | ".join(str(i + 1) for i in range(self.size)) + " |"

        for i, row in enumerate(self.fields):
            string += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hidden:
            string = string.replace("■", "O")

        return string

    def out(self, dot):
        return not ((0 <= dot.x < self.size) and (0 <= dot.y < self.size))

    def shot(self, dot):
        if dot in self.shotted_dots:
            raise BoardAlreadyShottedException()

        if self.out(dot):
            raise BoardShootOffException()

        self.shotted_dots.append(dot)

        for ship in self.ships:
            if ship.hit(dot):
                self.fields[dot.x][dot.y] = "X"
                if ship.destroyed():
                    print("The ship is destroyed!")
                    self.contour(ship, True)
                    for ship_dot in ship.contour_dots:
                        self.fields[ship_dot.x][ship_dot.y] = "."
                    return False
                else:
                    print("The ship is hit!")
                    return True
            else:
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
