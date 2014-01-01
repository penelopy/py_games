#started Dec 26

import pygame, sys, random
from settings import *
from classes import *
from pygame.locals import *


def run_game(): 
	pygame.init()
	
	x = 200
	y = 80
	move_x = 7
	move_y = 5
	phase = 1
	x_phase = 1
	pygame.display.set_caption('Pong Ball')
	pygame.display.update()


	while program_running == True: 
		
		while game_in_progress ==True:
		
			pygame.display.update()
			
	# 		# Wait for input
			mouseClicked = False
			while mouseClicked == False: 
				
				if y >= 570:
					phase = 1
				if y <= 30:
					phase = 2
				if phase == 1:
					y -= move_y
				if phase == 2: 
					y += move_y

				if x >= 870:
					x_phase = 1
				if x <= 30:
					x_phase = 2
				if x_phase == 1:
					x -=move_x
				if x_phase == 2: 
					x += move_x

				screen.fill(GRAY)
				pygame.draw.circle(screen, CYAN, (x, y), 40, 0)
				pygame.time.wait(20)
				pygame.display.update()

				for event in pygame.event.get(): 
					keys = pygame.key.get_pressed() 
					if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
						pygame.quit()
						sys.exit()

	



run_game()
