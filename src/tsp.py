from logic.cities import calculate_distance, calculate_total_distance, routes_to_cities
import pygame 
import sys

from pygame_functions.graphics import draw_text, draw_cities
from data.cities import cities_locations

# Define constant values
# pygame
WIDTH, HEIGHT = 800, 400
NODE_RADIUS = 5
FPS = 30
PLOT_X_OFFSET = 450

N_CITIES = 15

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSP Solver using Pygame")
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    screen.fill(WHITE)
    
    draw_cities(screen, cities_locations[N_CITIES], RED, NODE_RADIUS)
    city1 = cities_locations[N_CITIES][0]
    city2 = cities_locations[N_CITIES][1]
    distance = calculate_distance(city1,city2)
    draw_text(screen, f"Distance: {distance}", BLACK, city1[0], city1[1])
    total_distance = calculate_total_distance(cities_locations[N_CITIES])
    draw_text(screen, f"Total distance: {total_distance}", BLACK, 5, 350)
    draw_text(screen, "TSP Solver - Press Q to quit", BLACK, 5, 380)
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()