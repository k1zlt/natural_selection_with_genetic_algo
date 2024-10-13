import random as ran


class Agent:
    def __init__(self, x, y, speed_x=1, speed_y=1):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def get_position(self):
        return (self.x, self.y)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def reproduce(self):
        return [
            Agent(
                self.x,
                self.y,
                self.speed_x + (ran.random() - 0.5),
                self.speed_y + (ran.random() - 0.5),
            ),
            Agent(
                self.x,
                self.y,
                self.speed_x + (ran.random() - 0.5),
                self.speed_y + (ran.random() - 0.5),
            ),
        ]

    def __str__(self):
        return f"Agent at position ({self.x}, {self.y}) with speed ({self.speed_x}, {self.speed_y})"
