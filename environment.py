from agent import Agent


class Environment:
    def __init__(self, radius, x=0, y=0):
        self.radius = radius
        self.x = x
        self.y = y

    def get_distance(self, agent: Agent):
        distance = ((agent.x - self.x) ** 2 + (agent.y - self.y) ** 2) ** 0.5
        return distance

    def is_inside_circle(self, agent: Agent):
        distance = self.get_distance(agent)
        return distance <= self.radius

    def move_circle(self, dx, dy):
        self.x += dx
        self.y += dy
