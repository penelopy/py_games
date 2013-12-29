from settings import*
from classes import *



def draw_fixed_objs():
	# Displays unchanging screen decorations
	# Displays game box
	game = Rectangle(game_x, game_y, game_w, game_h, MATT_03)
	game.display()
	# Displays instruction box and blit text in box
	instr = Rectangle(instr_x, instr_y, instr_w, instr_h, MATT_02)
	instr.display()
	instr_text_loc = (instr.horz_center - instr_font.size("Does the Box 1 word match the Box 2 font color?")[0]/2, instr_y + 15)
	button_text("Does the Box 1 word match the Box 2 font color?", instr_text_loc, BLACK, 18)
	#Displays scoreboard
	display_sb = Rectangle(banner_x, banner_y, banner_w, banner_h, MATT_01)
	display_sb.display()
	display_scoreboard_text(rounds_text_loc, max_rounds_text_loc, true_answers_text_loc, false_answers_text_loc, score_text_loc)
	# Displays card labels
	button_text("Box 1", card1_label, BLACK, box_label_text_height)
	button_text("Box 2", card2_label, BLACK, box_label_text_height)
	# Displays yes button and instructions
	yes_button = Rectangle(yes_button_x, yes_button_y, yes_button_w, yes_button_h, MATT_04)
	yes_button.display()
	button_text("Click box or use left arrow", yes_button_note, BLACK, 15)

	# Displays no button and instructions
	no_button = Rectangle(no_button_x, no_button_y, no_button_w, no_button_h, MATT_04)
	no_button.display()
	button_text("Click box or use right arrow", no_button_note, BLACK, 15)
	# Blits text in Yes and No buttons
	yes_text_loc = (yes_button.horz_center - y_button_font.size("YES")[0]/2, yes_button.vert_center - text_height/2)
	no_text_loc = (no_button.horz_center - y_button_font.size("NO")[0]/2, no_button.vert_center - text_height/2)
	button_text("YES", yes_text_loc, BLACK, 24)
	button_text("NO", no_text_loc, BLACK, 24)





