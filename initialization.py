from environment import Environment
from agent import Agent
import random

environment = Environment(radius=10, x=0, y=0)

agents = []
num_agents = 5

for _ in range(num_agents):
    # Generate random coordinates within the circle
    while True:
        x = random.uniform(-environment.radius, environment.radius)
        y = random.uniform(-environment.radius, environment.radius)
        # Create an agent with random speed
        speed_x = random.uniform(0.5, 2)
        speed_y = random.uniform(0.5, 2)
        agent = Agent(x, y, speed_x, speed_y)
        if environment.is_inside_circle(agent):
            break
    agents.append(agent)

