"""
File: template.py
Author: Your Name
Date: 2024-03-20
Description: Template for basic Pygame graphics setup.
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PyGame Patterns")

# Define colours from https://www.pygame.org/docs/ref/color_list.html
WHITE = pygame.Color("white")
BLACK = pygame.Color("gray0")
BLUE = pygame.Color("aqua")

# Main loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw graphics - BEGIN YOUR PROGRAM HERE
    screen.fill(WHITE)

    #Grid pattern
    for x_pos in range(0, 401, 40):
        pygame.draw.line(screen, BLACK, (x_pos, 0), (x_pos, 400))
    for y_pos in range(0, 401, 40):
        pygame.draw.line(screen, BLACK, (0, y_pos), (400, y_pos))
    
    # Circle Pattern
    for y_pos in range(50, 401, 100):
        pygame.draw.circle(screen, BLUE, (445, y_pos), 15)
    for y_pos in range(50, 401, 100):
        pygame.draw.circle(screen, BLUE, (545, y_pos), 15)
    for y_pos in range(50, 401, 100):
        pygame.draw.circle(screen, BLUE, (645, y_pos), 15)
    for y_pos in range(50, 401, 100):
        pygame.draw.circle(screen, BLUE, (745, y_pos), 15)

    # Gradient
    black = (0, 0, 0)
    dark_grey = (16, 16, 16)
    light_grey = (127, 127, 127)
    white = (255, 255, 255)
    for x_pos in range(0, 101, 1):
        pygame.draw.line(screen, black, (x_pos, 401), (x_pos, 800))
    

    
    



    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
