class Point:

    x, y = 0, 0

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)

    def dot(self, p: "Point"):
        return self.x * p.x + self.y * p.y
