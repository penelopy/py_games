#started Dec 26

import pygame, sys, random
from settings import *
from classes import *
from pygame.locals import *
from Draw_Fixed_Obj import *



def run_game(): 
	pygame.init()
	screen.fill(GRAY)
	
	draw_fixed_objs()

	pygame.display.set_caption('Flash Cards')
	pygame.display.update()

	while program_running == True: 
		global game_in_progress
		while game_in_progress ==True:
			# Displays randomly generated text and color onto flash card
			correct_answer = flash_card()
		
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

						# Depending on which button (Y/N) was clicked, assigns user_input
						if is_yes_button:
							user_input = True
						elif is_no_button:
							 user_input = False
					# Allows game play using Right and Left keyboard strokes
					if event.type == pygame.KEYDOWN:
						if keys[pygame.K_LEFT]: 
							user_input = True
							mouseClicked = True	
						if keys[pygame.K_RIGHT]: 
							user_input = False
							mouseClicked = True	
					

			is_answer_correct(user_input, correct_answer)

			
			display_sb = Rectangle(banner_x, banner_y, banner_w, banner_h, MATT_01)
			display_sb.display()
			display_scoreboard_text(rounds_text_loc, max_rounds_text_loc, true_answers_text_loc, false_answers_text_loc, score_text_loc)
			display_score() 

			if number_of_rounds == current_no_of_rounds: 
				# game_in_progress = False
				game_over()


# wait for input
	mouseClicked = False
	while mouseClicked == False: 
		for event in pygame.event.get(): 
			keys = pygame.key.get_pressed()
			if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()	


def is_answer_correct(user_input, correct_answer): 
	# Reviews whether answer is correct and increment score
	global score 
	global false_answers
	global true_answers
	global current_no_of_rounds
	if user_input == correct_answer: 
		score += 10
		true_answers += 1
	elif user_input != correct_answer: 
		false_answers +=1
	#increment current_no_of_rounds	
	current_no_of_rounds += 1

def display_score():		
	data_right_edge = game_x - border
	# Writes and displays score to screen
	score_data = button_text(str(score), (data_right_edge - scoreb_font.size(str (score))[0], score_text_loc[1]), BLACK,scoreb_font_size)
	# Writes and displays Current # of rounds to screen
	curr_rounds_data = button_text(str(current_no_of_rounds), (data_right_edge - scoreb_font.size(str (current_no_of_rounds))[0], rounds_text_loc[1]), BLACK,scoreb_font_size)
	# Writes and displays Max # of Rounds to screen
	max_rounds_data = button_text(str(max_no_rounds), (data_right_edge - scoreb_font.size(str (max_no_rounds))[0], max_rounds_text_loc[1]), BLACK,scoreb_font_size)
	# Writes and displays # True Answers to screen
	true_answers_data = button_text(str(true_answers), (data_right_edge - scoreb_font.size(str (true_answers))[0], true_answers_text_loc[1]), BLACK,scoreb_font_size)
	# Writes and displays # of False answers to screen
	false_answers_data = button_text(str(false_answers), (data_right_edge - scoreb_font.size(str (false_answers))[0], false_answers_text_loc[1]), BLACK,scoreb_font_size)

def game_over():
	game_in_progress = False
	display_sb = Rectangle(banner_x, banner_y, banner_w, banner_h, MATT_01)
	display_sb.display()
	display_scoreboard_text(rounds_text_loc, max_rounds_text_loc, true_answers_text_loc, false_answers_text_loc, score_text_loc)
	display_score()
	button_text("GAME OVER", (banner_x + 15, banner_y + 270), BLACK, 24)

run_game()
