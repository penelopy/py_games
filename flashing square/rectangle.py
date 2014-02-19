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
		# self.right = self.x + self.width
		# self.bottom = self.y + self.height
		# self.hover = False
		# self.click = False
		# self.grab = False
		# self.drop = False
		# self.is_in_box = False


	def display(self):
		pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])	
		pygame.draw.rect(screen, BLACK, [self.x, self.y, self.width, self.height], 1)


# def button_text(text_display, (location_x, location_y), color=BLACK, font_size=30):
# 	myfont = pygame.font.SysFont("Arial", font_size)
# 	label = myfont.render(text_display, 1, color)
# 	screen.blit(label, (location_x, location_y))


class Flash():
	def __init__(self, x, y, width, height, color, speed):
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.speed = speed

	def display(self):
		pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])	
		pygame.draw.rect(screen, BLACK, [self.x, self.y, self.width, self.height], 1)

	def move(self):
		if self.x < x_end and self.y == y_start:
			self.x += self.speed
			return
		elif self.x == x_end and self.y < y_end:
			self.y += block_h
			return
		if self.x > x_start and self.y == y_end:
			self.x -= block_w
			return
		elif self.x == x_start and self.y > y_start:
			self.y -= block_h
			return


# box_1 = Flash(10, 10, BLUE)
# box_1.move()

	


