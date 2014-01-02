import pygame, sys, random
pygame.init()


# Screen parameters
screen_width, screen_height = 900, 600
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

border = 25
font_size = 18
myfont = pygame.font.SysFont("Arial", font_size)

# Set up the colors
BLACK = ( 0, 0, 0)
CYAN = (  0, 255, 255)

ROSE1 = (253, 47, 88)
ROSE = (220, 176, 173)
BRICK = (132, 68, 72)


# Set up mouse and click positions
click_position = [0, 0]
click_positions = []
mousex = 0 # used to store x coordinate of mouse event
mousey = 0 # used to store y coordinate of mouse event
mouseClicked = False
game_in_progress = True
program_running = True


text_display = " "





