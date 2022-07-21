from dot import Dot


class Ship:
    def __init__(self, length, x, y, direction):
        self.length = length
        self.hp = length
        self.x = x
        self.y = y
        self.direction = direction

    @property
    def dots(self):
        dots = []

        if self.direction == 'horizontal':
            for x in list(range(self.x, self.x+self.length)):
                dots.append(Dot(x, self.y))
        elif self.direction == 'vertical':
            for y in list(range(self.y, self.y+self.length)):
                dots.append(Dot(self.x, y))

        return dots

    @property
    def contour_dots(self):
        contour_dots = []
        for dot in self.dots:
            for sibling in dot.siblings:
                if sibling not in contour_dots and sibling not in self.dots:
                    contour_dots.append(sibling)

        return contour_dots

    def hit(self, dot):
        if dot in self.dots:
            self.hp -= 1
            return True

        return False

    def destroyed(self):
        return self.hp <= 0

