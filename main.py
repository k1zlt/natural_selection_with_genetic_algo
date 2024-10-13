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
d = 1.5
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Check for arrow key presses and adjust position accordingly
    if keys[pygame.K_LEFT]:
        env.x -= d
    if keys[pygame.K_RIGHT]:
        env.x += d
    if keys[pygame.K_UP]:
        env.y -= d
    if keys[pygame.K_DOWN]:
        env.y += d

    screen.fill(RED)

    # Drawing
    pygame.draw.circle(screen, WHITE, (env.x, env.y), env.radius)
    agents = update(environment=env, agents=agents)
    for i in agents:
        pygame.draw.circle(screen, (0, 0, 0, int(i.live / i.live_constant)*255), (i.x, i.y), 3)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
