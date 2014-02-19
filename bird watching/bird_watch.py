#started Dec 26
#posted to github on Dec 29

import pygame, sys, random, math
from math import sqrt
from settings import *
from classes import *
from pygame.locals import *



def run_game(): 
	pygame.init()
	screen.fill(GREEN)
	# barn = Animal((700, 480), "barn_v002.png")
	cat = Animal(cat_position, "grey_cat.png")
	bird = Animal(bird_position, "bluebird_3.png")
	pygame.draw.rect(screen, BLUE, (0, 0, screen_width, 300))
	pygame.mixer.music.load("kitten4.wav")
	pygame.mixer.music.play(-1,0.0)

	pygame.display.set_caption('Bird Watching')
	pygame.display.update()


	while program_running == True: 
		
		while game_in_progress ==True:
		
			pygame.display.update()
			
			# Wait for input
			mouseClicked = False
			while mouseClicked == False: 
				screen.fill(GREEN)
				pygame.draw.rect(screen, SKY, (0, 0, screen_width, 525))
				cat.draw()
				bird.move()
				bird.draw()
				# barn.draw()


				left_eye = Circle(245, 330, 14, WHITE)
				left_eye.display()
				right_eye = Circle(360, 328, 14, WHITE)
				right_eye.display()

				left_pupil = Pupil(bird, 242, 330)
				left_pupil.x = 242
				left_pupil.y = 330
				left_pupil.radius = 2
				left_pupil.calculate_position()	

				right_pupil = Pupil(bird, 358, 328)
				right_pupil.x = 362
				right_pupil.y = 333
				right_pupil.radius = 10
				right_pupil.calculate_position()

				
				# pygame.time.wait(30)
				pygame.display.update()
				look_for_quit()



def look_for_quit():
	for event in pygame.event.get(): 
		keys = pygame.key.get_pressed() 
		if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()


	

run_game()
