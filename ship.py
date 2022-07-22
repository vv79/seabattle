from dot import Dot


class Ship:
    def __init__(self, length, x, y, direction):
        self.length = length
        self.hp = length
        self.x = x
        self.y = y
        self.direction = direction

    def __repr__(self):
        return f'{self.x}:{self.y}:{self.length}:{self.direction}'

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.length):
            cur_x = self.x
            cur_y = self.y

            if self.direction == 'horizontal':
                cur_x += i

            elif self.direction == 'vertical':
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def hit(self, dot):
        if dot in self.dots:
            self.hp -= 1
            return True

        return False

    def destroyed(self):
        return self.hp <= 0

