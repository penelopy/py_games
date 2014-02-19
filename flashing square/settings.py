import pygame, sys, random
pygame.init()


# Screen parameters
screen_width, screen_height = 775, 550
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
bg_color = 200, 200, 200


num_block_x = 8
num_block_y = 4
block_w = 50
block_h = 50
x_start = 10
y_start = 10
x_end = x_start + (num_block_x * block_w)
y_end = y_start + (num_block_y * block_h)

font_size = 18
myfont = pygame.font.SysFont("Arial", font_size)

# Set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (126, 126, 126) 
ORANGE1 = (255, 177, 61)
ORANGE = (255, 145, 36)
ORANGE2 = (255, 223, 128)
BLUE2 = (0, 230, 230)
BLUE = (70, 145, 200)
ORANGE3 = (230, 115, 0)


game_in_progress = True
program_running = True


text_display = " "

# Define gamebox dimensions
game_x = 25
game_y = 25
game_w = 100
game_h = 100 
game_color = ORANGE


