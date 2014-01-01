from settings import *
import pygame, sys, random
pygame.init()


class Rectangle():
	def __init__(self, x, y, width, height, color):
		self.color = color
		self.x = x
		self.y = y
		self.x_home = x 
		self.y_home = y 
		self.width = width
		self.height = height
		self.right = self.x + self.width
		self.bottom = self.y + self.height
		self.hover = False
		self.click = False
		self.grab = False
		self.drop = False
		self.is_in_box = False


	def display(self):
		pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])	
		pygame.draw.rect(screen, BLACK, [self.x, self.y, self.width, self.height], 1)

	def detect_hover(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		self.right = self.x + self.width
		self.bottom = self.y + self.height
		if mouse_x > self.x and mouse_x < self.right and mouse_y > self.y and mouse_y < self.bottom:
			self.hover = True

		else:
			self.hover = False

	def detect_grab(self):
		if pygame.mouse.get_pressed()[0] == 1:
			click = True
		else:
			click = False
		# if hover is detected, leave it on indefinitely, until a drop is detected.  This prevents the grab from being canceled if the mouse moves faster than the screen can detect.
		self.detect_hover()
		if click == True and self.hover == True:
			self.grab = True
		if self.grab == True:	
			self.x = pygame.mouse.get_pos()[0] - self.width/2
			self.y = pygame.mouse.get_pos()[1] - self.height/2 

	def detect_drop(self):
		if pygame.mouse.get_pressed()[0] == 0 and self.grab == True:
			self.grab = False
			self.drop = True
			#remember to set it to false after you perform the drop action

	def detect_in_box(self):
		if self.x > game_x and self.x < game_x + game_w - block and self.y > game_y and self.y < game_y + game_h - block:
			self.is_in_box = True
			self.grab = False
			self.x = self.x_home
			self.y = self.y_home
		else:
			self.is_in_box = False



def button_text(text_display, (location_x, location_y), color=BLACK, font_size=30):
	myfont = pygame.font.SysFont("Arial", font_size)
	label = myfont.render(text_display, 1, color)
	screen.blit(label, (location_x, location_y))





	


