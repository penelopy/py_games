#started Jan 11

import pygame, sys, random
from settings import *
from rectangle import *
from pygame.locals import *


def run_game(): 
	pygame.init()
	
	pygame.display.set_caption('Chasing Squares')
	pygame.display.update()
	screen.fill(ORANGE3)

	border_boxes(x_start,y_start, block_w, block_h, num_block_x,True)
	border_boxes(x_end,y_start, block_w, block_h, num_block_y,False)
	border_boxes(x_start,y_end, block_w, block_h, num_block_x,True)
	border_boxes(x_start,y_start, block_w, block_h, num_block_y,False)

	pygame.display.update()
	num_chickens = 4
	chicken_array = []
	flash_start_array = [(x_start,y_start), (x_end,y_start), (x_end,y_end), (x_start,y_end)]
	block_color = [50,125,200]
	for i in range(0,num_chickens):
		block_color[0] += 5
		block_color[1] += 5
		block_color_new = tuple(block_color)
		chicken = Flash(flash_start_array[i][0], flash_start_array[i][1], block_w, block_h, block_color_new, block_w)
		chicken_array.append(chicken)
		# box_2 = Flash(410, 10, block_w, block_h, WHITE, 100)	



	while program_running == True: 
		look_for_quit()
		screen.fill(ORANGE3)
		border_boxes(x_start,y_start, block_w, block_h, num_block_x,True)
		border_boxes(x_end,y_start, block_w, block_h, num_block_y,False)
		border_boxes(x_start,y_end, block_w, block_h, num_block_x,True)
		border_boxes(x_start,y_start, block_w, block_h, num_block_y,False)

		for i in range(0,num_chickens):
			chicken_array[i].display()
			chicken_array[i].move()


		# box_1.move()
		# box_1.display()
		# box_2.move()
		# box_2.display()

		pygame.display.update()
		pygame.time.wait(100)


def look_for_quit():
	for event in pygame.event.get(): 
		keys = pygame.key.get_pressed() 
		if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()


def border_boxes(x,y,block_w, block_h, num_blocks,horiz_or_vert): #horiz_or_vert is a boolean that creates a horizontal row of boxes if True, and a vertical column of boxes if False
	for i in range(0, num_blocks +1):
		if horiz_or_vert == True:
			top_rect = Rectangle(x+(i*block_w), y, block_w, block_h, ORANGE3)
			top_rect.display()
		else:
			left_rect = Rectangle(x, y+(i*block_h), block_w, block_h, ORANGE3)
			left_rect.display()


run_game()
