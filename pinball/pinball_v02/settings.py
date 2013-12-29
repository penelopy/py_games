import pygame, sys, random
pygame.init()


# Screen parameters
screen_width, screen_height = 900, 600
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
font_size = 18
myfont = pygame.font.SysFont("Arial", font_size)

# Set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 153, 0)
BLUE = (51, 51, 255)
GRAY = (126, 126, 126) 
CYAN = (  0, 255, 255)
SLATE = (112, 128, 144)


game_in_progress = True
program_running = True


text_display = " "

# Define scoreboard box dimensions
left_col_x = 0
left_col_y = 0
left_col_width = 150
left_col_height = 600 

# Define barrier1 dimensions
barrier1_x = 400
barrier1_y = 100
barrier1_width = 40
barrier1_height = 150 
barrier1_right = barrier1_x + barrier1_width
barrier1_bottom = barrier1_y + barrier1_height

# Define barrier2 dimensions
barrier2_x = 400
barrier2_y = 400
barrier2_width = 150
barrier2_height = 40
barrier2_right = barrier2_x + barrier2_width
barrier2_bottom = barrier2_y + barrier2_height


# Define barrier3 dimensions
barrier3_x = 600
barrier3_y = 300
barrier3_width = 150
barrier3_height = 40 
barrier3_right = barrier3_x + barrier2_width
barrier3_bottom = barrier3_y + barrier3_height


# Define winner box dimensions
win_box_x = 750
win_box_y = 400
win_box_width = 75
win_box_height = 75
win_box_color = SLATE

# Define winner textbox dimensions
text_box_x = 650
text_box_y = 75
text_box_width = 200
text_box_height = 75




