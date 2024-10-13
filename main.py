import pygame
import sys

# from agent import Agent
# from environment import Environment
from initialization import environment
from initialization import agents as init_agents
from update import update

# Slider variables
slider_x = 50
slider_y = 100
slider_width = 300
slider_height = 5
slider_pos = slider_x
slider_radius = 10
reproduction_chance_min_val = 0
reproduction_chance_max_val = 1
reproduction_current_val = 0.01
reproduction_chance_dragging = False

# Function to draw slider
def draw_slider(slider_x, slider_y, slider_width, slider_height, slider_pos, slider_radius, title, current_val):
    # Draw the slider track
    pygame.draw.rect(screen, GRAY, (slider_x, slider_y, slider_width, slider_height))
    
    # Draw the slider handle
    pygame.draw.circle(screen, GREEN, (slider_pos, slider_y + slider_height // 2), slider_radius)
    
    # Render the current value
    font = pygame.font.SysFont(None, 36)
    value_surf = font.render(f"{title}: {current_val}", True, BLACK)
    screen.blit(value_surf, (slider_x, slider_y - 50))

def check_slider_event(event, slider_x, slider_y, slider_pos, slider_radius, slider_height, dragging, max_val, min_val, current_val):
    print(current_val)
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = event.pos
        if abs(mouse_x - slider_pos) < slider_radius and abs(mouse_y - (slider_y + slider_height // 2)) < slider_radius:
            dragging = True
            
    if event.type == pygame.MOUSEBUTTONUP:
        dragging = False
    
    if event.type == pygame.MOUSEMOTION:
        if dragging:
            mouse_x, _ = event.pos
            slider_pos = max(slider_x, min(mouse_x, slider_x + slider_width))
            current_val = ((slider_pos - slider_x) / slider_width * (max_val - min_val) + min_val)
    return dragging, current_val, slider_pos

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
agents = init_agents
running = True
d = 3


while running:
    x = 0
    y = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        reproduction_chance_dragging, reproduction_current_val, slider_pos = check_slider_event(event, slider_x, slider_y, slider_pos, slider_radius, slider_height, reproduction_chance_dragging, reproduction_chance_max_val, reproduction_chance_min_val, reproduction_current_val)
        

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

    screen.fill(RED)
    draw_slider(
        slider_x = slider_x, 
        slider_y = slider_y,
        slider_width = slider_width, 
        slider_height = slider_height, 
        slider_pos = slider_pos, 
        slider_radius = slider_radius, 
        current_val = reproduction_current_val, 
        title = "Reproduction Chance"
        )

    # Drawing
    pygame.draw.circle(screen, WHITE, (env.x, env.y), env.radius)
    agents = update(environment=env, agents=agents, reproduction_chance = reproduction_current_val)
    for i in agents:
        i.x -= x
        i.y -= y
        pygame.draw.circle(screen, BLACK, (i.x, i.y), 3)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
