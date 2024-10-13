import random as ran


class Agent:
    def __init__(self, x, y, speed_x=1, speed_y=1, live_constant=500):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.live_constant = live_constant
        self.live = live_constant
        self.fitness = 0

    def is_alive(self):
        return self.live > 0

    def get_position(self):
        return (self.x, self.y)

    def get_fitness(self, environment):
        return environment.radius - environment.get_distance(self)

    def move(self, environment):
        self.x += self.speed_x
        self.y += self.speed_y
        self.live -= 1
        self.fitness = self.get_fitness(environment)

    def reproduce(
        self, amount=2, mutation_rate=1, mutation_chance=1, live_constant=200
    ):
        get_random = lambda: 0
        if ran.random() < mutation_chance:
            get_random = lambda: ran.random()
        return [
            Agent(
                self.x,
                self.y,
                self.speed_x + mutation_rate * (get_random() - 0.5),
                self.speed_y + mutation_rate * (get_random() - 0.5),
                live_constant,
            )
        ] * amount

    def __str__(self):
        return f"Agent at position ({self.x}, {self.y}) with speed ({self.speed_x}, {self.speed_y})"
