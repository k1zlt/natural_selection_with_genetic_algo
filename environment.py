class Environment:
    def __init__(self, radius, x=0, y=0):
        self.radius = radius
        self.x = x
        self.y = y

    def is_inside_circle(self, x, y):
        distance = ((x - self.x) ** 2 + (y - self.y) ** 2) ** 0.5
        return distance <= self.radius

    def move_circle(self, dx, dy):
        self.x += dx
        self.y += dy
