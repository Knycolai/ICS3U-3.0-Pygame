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
    for x_pos in range(0, 401, 40):
        pygame.draw.line(screen, BLACK, (x_pos, 0), (x_pos, 400))
    for y_pos in range(0, 401, 40):
        pygame.draw.line(screen, BLACK, (0, y_pos), (400, y_pos))
    pygame.draw.line(screen, BLACK, (0, 40), (400, 40))
    for x_pos in range(450, 801, 100):
        pygame.draw.circle(screen, BLUE, (x_pos, 100), 15)
    for y_pos in range(100, 401, 100):
        pygame.draw.circle(screen, BLUE, (450, y_pos), 15)
    

    
    



    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
