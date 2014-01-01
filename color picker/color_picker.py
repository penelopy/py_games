#started Dec 31

import pygame, sys, random
from settings import *
from rectangle import *
from pygame.locals import *


def run_game(): 
	pygame.init()
	
	pygame.display.set_caption('Color Picker')
	pygame.display.update()
	screen.fill(ORANGE3)

	game_box = Rectangle(game_x, game_y, game_w, game_h, game_color)
	game_box.display()
	instr_box = Rectangle(0, 500, 800, 125, BLUE)
	instr_box.display()

	block_array = []
	block_x = 10
	block_y = 450
	block_w = 25
	block_h = 25
	block_color = [50,125,200]
	for i in range (1,25):
		block_x += int((block_w *1.2))
		block_color[0] += 5
		block_color[1] += 5
		block_color_new = tuple(block_color)
		myblock = Rectangle(block_x, block_y, block_w, block_h, block_color_new)
		block_array.append(myblock)
		myblock.display()
	pygame.display.update()

	while program_running == True: 
		look_for_quit()

		def block_movement(block): 
			block.detect_hover()
			block.detect_grab()
			block.detect_drop()
			block.detect_in_box()
			if block.is_in_box == True: 
				game_box.color = block.color

		for i in range (0, len(block_array)):
			block_movement(block_array[i])


		screen.fill(ORANGE)
		game_box.display()
		instr_box.display()
		button_text("Click and drag a color block into the large box.", (100, 525), BLACK, 26)

		for i in range (0, len(block_array)):
			block_array[i].display()

		pygame.display.update()



def look_for_quit():
	for event in pygame.event.get(): 
		keys = pygame.key.get_pressed() 
		if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()



run_game()
