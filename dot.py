class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = ''

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'{self.x+1}:{self.y+1}'

    @property
    def siblings(self):
        return [Dot(self.x - 1, self.y), Dot(self.x + 1, self.y), Dot(self.x, self.y - 1),
                Dot(self.x, self.y + 1), Dot(self.x - 1, self.y + 1),
                Dot(self.x - 1, self.y - 1), Dot(self.x + 1, self.y + 1), Dot(self.x + 1, self.y - 1)]
