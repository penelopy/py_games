import pygame, sys, random
pygame.init()


# Screen parameters
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
bg_color = 200, 200, 200
border = 15
block = 50

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

# Set up mouse and click positions
click_position = [0, 0]
click_positions = []
mousex = 0 # used to store x coordinate of mouse event
mousey = 0 # used to store y coordinate of mouse event
mouseClicked = False
game_in_progress = True
program_running = True


text_display = " "

# Define gamebox dimensions
game_x = 100
game_y = 25
game_w = 600
game_h = 400 #screen_height - (2 *block)
game_color = ORANGE


