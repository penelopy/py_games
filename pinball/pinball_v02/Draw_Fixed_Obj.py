from settings import*
from classes import *
	

def draw_fixed_objs():
	# Displays unchanging screen decorations

	#Displays scoreboard
	display_sb = Rectangle(left_col_x, left_col_y, left_col_width, left_col_height, CYAN)
	display_sb.display()

	#Displays barrier1
	barrier1 = Rectangle(barrier1_x, barrier1_y, barrier1_width, barrier1_height, CYAN)
	barrier1.display()

	# #Displays barrier2
	barrier2 = Rectangle(barrier2_x, barrier2_y, barrier2_width, barrier2_height, CYAN)
	barrier2.display()

	# #Displays barrier3
	barrier3 = Rectangle(barrier3_x, barrier3_y, barrier3_width, barrier3_height, CYAN)
	barrier3.display()

	#Displays win_box
	win_box = Rectangle(win_box_x, win_box_y, win_box_width, win_box_height, win_box_color)
	win_box.display()




	
	
	
	

