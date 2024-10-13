class Agent:
    def __init__(self, x, y, speed_x=1, speed_y=1):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def get_position(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx * self.speed_x
        self.y += dy * self.speed_y

    def __str__(self):
        return f"Agent at position ({self.x}, {self.y}) with speed ({self.speed_x}, {self.speed_y})"
