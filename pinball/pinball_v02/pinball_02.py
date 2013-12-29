#started Dec 26
#posted to github on Dec 29

import pygame, sys, random
from settings import *
from classes import *
from pygame.locals import *
from Draw_Fixed_Obj import *


x = 175
y = 80

move_x = 1
move_y = 1
x_previous = 0
y_previous = 0


def run_game(): 
	pygame.init()
	screen.fill(GREEN)
	draw_fixed_objs()

	pygame.display.set_caption('Pinball')
	pygame.display.update()


	while program_running == True: 
		
		while game_in_progress ==True:
		
			pygame.display.update()
			
			# Wait for input
			mouseClicked = False
			while mouseClicked == False: 
				
				screen.fill(GREEN)
				draw_fixed_objs()
				move_pinball()
				game_over()

				pygame.draw.circle(screen, BLACK, (x, y), 20, 0)
				pygame.draw.circle(screen, CYAN, (x, y), 21, 1)
				# pygame.time.wait(30)
				pygame.display.update()
				look_for_quit()



def look_for_quit():
	for event in pygame.event.get(): 
		keys = pygame.key.get_pressed() 
		if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()

def move_pinball(): 
	global x
	global y
	global move_x
	global move_y


	if y <= 0 or y >= 600:
		move_y = move_y * (-1) 
	if x <= 151 or x >=900:
		move_x = move_x * (-1)

	barrier_zone(barrier2_y, barrier2_bottom, barrier2_x, barrier2_right)
	barrier_zone(barrier1_y, barrier1_bottom, barrier1_x, barrier1_right)
	barrier_zone(barrier3_y, barrier3_bottom, barrier3_x, barrier3_right)

def barrier_zone(top_edge, bottom_edge, left_edge, right_edge):
	global y
	global move_y
	global x
	global move_x
	global x_previous 
	global y_previous 
	x_prev_in_x_band = False
	y_prev_in_y_band = False


	x_in_x_band = x >= left_edge and x <= right_edge
	y_in_y_band = y >= top_edge and y <= bottom_edge
	in_box = x_in_x_band and y_in_y_band
	x_prev_in_x_band = x_previous >= left_edge and x_previous <= right_edge
	y_prev_in_y_band = y_previous >= top_edge and y_previous <= bottom_edge


	if in_box:
		if x_prev_in_x_band: 
			move_y *= (-1)
		if y_prev_in_y_band: 
			move_x *= (-1)

		if not x_prev_in_x_band and not y_prev_in_y_band: 
			move_y *= (-1)			
			move_x *= (-1)


	y_previous = y
	y += move_y
	x_previous = x
	x += move_x

def game_over():
	global move_x
	global move_y

	in_x_band = x >= win_box_x and x <= win_box_x + win_box_width
	in_y_band = y >= win_box_y and y <= win_box_y + win_box_height
	in_game_box = in_x_band and in_y_band

	if in_game_box: 
		move_y *= 0
		move_x *= 0

		win_box_color = BLUE	

		count = 0
		while 1: 
			look_for_quit()
			count += 1
			remainder = count%10
			print remainder
			if remainder > 5: 
				win_box_color = RED
			else: 
				win_box_color = BLUE
			game_over_text()
			win_box = Rectangle(win_box_x, win_box_y, win_box_width, win_box_height, win_box_color)
			win_box.display()
			pygame.draw.circle(screen, BLACK, (win_box_x + win_box_width/2, win_box_y + win_box_height/2), 20, 0)
			pygame.draw.circle(screen, CYAN, (win_box_x + win_box_width/2, win_box_y + win_box_height/2), 21, 1)
			pygame.display.update()	

def game_over_text():
	text_box = Rectangle(text_box_x, text_box_y, text_box_width, text_box_height, WHITE)
	text_box.display()
	myfont = pygame.font.SysFont("Arial", 30)
	label = myfont.render("You Win!!", 1, BLACK)
	screen.blit(label, (text_box_x + 15, text_box_y +15))		

run_game()
