from environment import Environment
from agent import Agent
import random

environment = Environment(radius=150, x=800, y=450)

agents = []
num_agents = 100

for _ in range(num_agents):
    # Generate random coordinates within the circle
    while True:
        x = random.uniform(
            environment.x - environment.radius, environment.x + environment.radius
        )
        y = random.uniform(
            environment.y - environment.radius, environment.y + environment.radius
        )
        # Create an agent with random speed
        # speed_x = random.uniform(0.5, 2)
        # speed_y = random.uniform(0.5, 2)
        agent = Agent(x, y, 0, 0)
        if environment.is_inside_circle(agent):
            break
    agents.append(agent)
