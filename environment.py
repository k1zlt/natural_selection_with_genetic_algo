from agent import Agent
class Environment:
    def __init__(self, radius, center_x=0, center_y=0):
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y

    def is_inside_circle(self, agent: Agent):
        distance = ((agent.x - self.center_x) ** 2 + (agent.y - self.center_y) ** 2) ** 0.5
        return distance <= self.radius

    def move_circle(self, dx, dy):
        self.center_x += dx
        self.center_y += dy
