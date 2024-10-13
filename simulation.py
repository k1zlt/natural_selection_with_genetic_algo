from environment import Environment
from agent import Agent
import random

def main(): 
    # Create an environment (circle)
    env = Environment(radius=10, center_x=0, center_y=0)

    # Create agents inside the circle
    agents = []
    num_agents = 5

    for _ in range(num_agents):
        # Generate random coordinates within the circle
        while True:
            x = random.uniform(-env.radius, env.radius)
            y = random.uniform(-env.radius, env.radius)
            if env.is_inside_circle(x, y):
                break

        # Create an agent with random speed
        speed_x = random.uniform(0.5, 2)
        speed_y = random.uniform(0.5, 2)
        agent = Agent(x, y, speed_x, speed_y)
        agents.append(agent)

    # Print initial positions of agents
    print("Initial agent positions:")
    for agent in agents:
        print(agent)

    # Simulate movement for a few steps
    num_steps = 5
    for step in range(num_steps):
        print(f"\nStep {step + 1}:")
        for agent in agents:
            # Generate random movement
            dx = random.uniform(-1, 1)
            dy = random.uniform(-1, 1)
            agent.move(dx, dy)
            # Check if the agent is still inside the circle
            if not env.is_inside_circle(*agent.get_position()):
                # If outside, remove the agent
                agents.remove(agent)
            else:
                print(agent)


if __name__ == "__main__":
    main()
