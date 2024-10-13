import pygame
import sys
from agent import Agent
from environment import Environment
import random

pygame.init()

screen_width = 1600
screen_height = 900
center = [screen_width//2, screen_height//2]
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Starter")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

env = Environment(radius=150, x=center[0], y=center[1])

agents = []
num_agents = 50

for _ in range(num_agents):
    while True:
        x = random.uniform(env.x-env.radius, env.x+env.radius)
        y = random.uniform(env.y-env.radius, env.y+env.radius)
        speed_x = random.uniform(0.5, 2)
        speed_y = random.uniform(0.5, 2)
        agent = Agent(x, y, speed_x, speed_y)
        if env.is_inside_circle(agent):
            break
    
    agents.append(agent)
    
print("Initial agent positions:")
for agent in agents:
    print(agent)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    env.x, env.y = pygame.mouse.get_pos()
    
    
    
    screen.fill(RED)
    
    # Drawing
    pygame.draw.circle(screen, WHITE, (env.x, env.y), env.radius)
    
    for i in agents:
        pygame.draw.circle(screen, BLACK, (i.x, i.y), 3)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
