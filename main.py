import pygame
import sys

# from agent import Agent
# from environment import Environment
from initialization import environment
from initialization import get_agents
from sliders import get_sliders
from update import update

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
GRAY = (100, 100, 100)
GREEN = (0, 255, 0)

env = environment
agents = get_agents()
running = True
d = 3
sliders= get_sliders()


while running:
    x = 0
    y = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for slider in sliders:
            slider.handle_event(event)
    keys = pygame.key.get_pressed()
    # Check for arrow key presses and adjust position accordingly
    if keys[pygame.K_LEFT]:
        x -= d
    if keys[pygame.K_RIGHT]:
        x += d
    if keys[pygame.K_UP]:
        y -= d
    if keys[pygame.K_DOWN]:
        y += d
    if keys[pygame.K_SPACE]:
        agents = get_agents()

    screen.fill(RED)
    for slider in sliders:
        slider.draw(screen, colors=(GRAY, GREEN, BLACK))
    reproduction_chance = sliders[0].get_value()
    live_constant = sliders[1].get_value()
    mutation_rate = sliders[2].get_value()
    birth_amount = sliders[3].get_value()
    mutation_chance = sliders[4].get_value()
    limit = sliders[5].get_value()
    fitness_split = sliders[6].get_value()
    fitness_cleaning_prob = sliders[7].get_value()
    # Drawing
    pygame.draw.circle(screen, WHITE, (env.x, env.y), env.radius)
    agents = update(
        environment=env, agents=agents, reproduction_chance=reproduction_chance,
        live_constant=live_constant,
        mutation_rate=mutation_rate,
        birth_amount=birth_amount,
        mutation_chance=mutation_chance,
        limit=limit,
        fitness_split=fitness_split,
        fitness_cleaning_prob=fitness_cleaning_prob
    )
    for i in agents:
        i.x -= x
        i.y -= y
        pygame.draw.circle(screen, BLACK, (i.x, i.y), 3)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
