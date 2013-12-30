import pygame, sys, random
pygame.init()


# Screen parameters
screen_width, screen_height = 900, 600
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
cat_position = 100, 125
bird_position = 700, -10
font_size = 18
myfont = pygame.font.SysFont("Arial", font_size)

# Set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 153, 0)
SKY = (135, 206, 250)
BLUE = (51, 51, 255)
GRAY = (126, 126, 126) 
CYAN = (  0, 255, 255)
SLATE = (112, 128, 144)

AUTO_MOVE_DICT = {1 : (-40, 0),
               2 : (40, 0)}
               # 3 : ( 0,-block_width),
               # 4 : ( 0, block_width)}


game_in_progress = True
program_running = True



