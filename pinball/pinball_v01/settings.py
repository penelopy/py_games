import pygame, sys, random
pygame.init()


# Screen parameters
screen_width, screen_height = 900, 600
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
bg_color = 200, 200, 200
scoreboard_height = 50
border = 25
font_size = 18
myfont = pygame.font.SysFont("Arial", font_size)

# Set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 153, 0)
BLUE = (51, 51, 255)
YELLOW = (255, 255, 156)
LIME = (0, 255, 0)
GRAY = (126, 126, 126) 
CYAN = (  0, 255, 255)
SKY = (135, 206, 250)
SKY2 = (176, 226, 255)
SLATE = (112, 128, 144)
MATT_01 = (102,153,102)
MATT_02 = (102,153,128)
MATT_03 = (102,153,153)        
MATT_04 = (102,128,102)
MATT_05 = (192,192,192)
background_color = SLATE

# Set up game variables


# Set up mouse and click positions
click_position = [0, 0]
click_positions = []
mousex = 0 # used to store x coordinate of mouse event
mousey = 0 # used to store y coordinate of mouse event
mouseClicked = False
game_in_progress = True
program_running = True
number_of_rounds = 20 # this one works

max_no_rounds = 20 # this one is doing something else



# Define scoreboard box dimensions
banner_w = 350
banner_h = screen_height - (2 * border)
banner_x = border
banner_y = border

# Define gamebox dimensions
game_w = 500
game_h = screen_height - (2 *border)
game_x = banner_w + border -1
game_y = border 

# Define card1_rect dimensions
card1_rect_w = game_w - (2 * border)
card1_rect_h = 100
card1_rect_x = banner_w + (2 * border)
card1_rect_y = border + border + border

# Define card2_rect dimensions
card2_rect_w = game_w - (2 * border)
card2_rect_h = 100
card2_rect_x = banner_w + (2 * border)
card2_rect_y = card1_rect_y + card1_rect_h+ border + border

# Define yes_button dimensions
yes_button_w = (game_w - (3 * border))/2
yes_button_h = 75
yes_button_x = banner_w + (2 * border)
yes_button_y = card2_rect_y + card2_rect_h + border

# Define no_button dimensions
no_button_w = (game_w - (3 * border))/2
no_button_h = 75
no_button_x = yes_button_x + yes_button_w + (border)
no_button_y = card2_rect_y + card2_rect_h + border




