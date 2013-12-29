#started Dec 26

import pygame, sys, random
from settings import *
from classes import *
from pygame.locals import *
from test_modules import *
from Draw_Fixed_Obj import *



def run_game(): 
	pygame.init()
	screen.fill(GREEN)
	
	draw_fixed_objs()

	pygame.display.set_caption('Pinball')
	pygame.display.update()

	while program_running == True: 
		global game_in_progress
		while game_in_progress ==True:
			# Displays randomly generated text and color onto flash card
			
		
			pygame.display.update()

			
			# Wait for input
			mouseClicked = False
			while mouseClicked == False: 
				
				for event in pygame.event.get(): 
					keys = pygame.key.get_pressed() 

					if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
						pygame.quit()
						sys.exit()	
					if event.type == MOUSEBUTTONUP:
						mousex, mousey = event.pos
						# Identifies if yes or no button has been clicked
						is_yes_button = mousex >= yes_button_x and mousex < yes_button_x + yes_button_w and mousey >= yes_button_y and mousey <yes_button_y + yes_button_h
						is_no_button = mousex >= no_button_x and mousex < no_button_x + no_button_w and mousey >= no_button_y and mousey < no_button_y + no_button_h
						if is_yes_button or is_no_button:
							mouseClicked = True	

					# Allows game play using Right and Left keyboard strokes
					if event.type == pygame.KEYDOWN:
						if keys[pygame.K_LEFT]: 
							user_input = True
							mouseClicked = True	
						if keys[pygame.K_RIGHT]: 
							user_input = False
							mouseClicked = True	
					



# wait for input
	mouseClicked = False
	while mouseClicked == False: 
		for event in pygame.event.get(): 
			keys = pygame.key.get_pressed()
			if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()	




run_game()
