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
        dots = []

        if self.direction == 'horizontal':
            for x in range(self.length):
                dots.append(Dot(x, self.y))
        elif self.direction == 'vertical':
            for y in range(self.length):
                dots.append(Dot(self.x, y))

        return dots

    def hit(self, dot):
        print(self.dots)
        if dot in self.dots:
            self.hp -= 1
            return True

        return False

    def destroyed(self):
        return self.hp <= 0

