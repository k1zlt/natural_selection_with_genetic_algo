import pygame
import sys

# from agent import Agent
# from environment import Environment
from initialization import environment
from initialization import agents as init_agents
from update import update

# import random

pygame.init()

screen_width = 1600
screen_height = 900
center = [screen_width // 2, screen_height // 2]
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Starter")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

env = environment
agents = init_agents
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    env.x, env.y = pygame.mouse.get_pos()

    screen.fill(RED)

    # Drawing
    pygame.draw.circle(screen, WHITE, (env.x, env.y), env.radius)
    agents = update(environment=env, agents=agents)
    for i in agents:
        pygame.draw.circle(screen, BLACK, (i.x, i.y), 3)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
