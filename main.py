import pygame
import sys
from agent import Agent

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Starter")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

env = Environment(radius=10, center_x=screen_width//2, center_y=screen_height//2)

agents = []
num_agents = 5

for _ in range(num_agents):
    while True:
        x = random.uniform(-env.radius, env.radius)
        y = random.uniform(-env.radius, env.radius)
        if env.is_inside_circle(x, y):
            break
    speed_x = random.uniform(0.5, 2)
    speed_y = random.uniform(0.5, 2)
    agent = Agent(x, y, speed_x, speed_y)
    agents.append(agent)
    
print("Initial agent positions:")
for agent in agents:
    print(agent)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
