from settings import *
import pygame, sys, random, math
from math import sqrt
pygame.init()


class Circle():
	def __init__(self, x, y, radius, color, width=0):
		self.color = color
		self.x = x
		self.y = y
		self.radius = radius
		self.width = width

	def display(self):
		# pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.width)

class Pupil(): 
	def __init__(self, bird, eye_x, eye_y):
		self.x = 0
		self.y = 0 
		self.radius = 0 
		self.bird = bird
		self.eye_x = eye_x
		self.eye_y = eye_y

	def calculate_position(self): 
		X = self.bird.x - self.eye_x 
		Y = self.bird.y - self.eye_y 
		Z = sqrt(X**2 + Y**2)

		z = 14
		x = int(X*z/Z)
		y = int(Y*z/Z)

		# draw pupil
		pygame.draw.circle(screen, BLACK, (self.eye_x + int(x), self.eye_y + int(y)), 8, 0)


	def draw(self):
		self.circle = Circle(self.x, self.y, self.radius, BLACK)
		self.circle.display()

class Animal(): 
	def __init__(self, animal_position, image_file):
		self.animal_position = animal_position
		self.image_file = image_file
		self.image = pygame.image.load(self.image_file)
		self.x = 700
		self.y = 0 

	def move(self):
		self.x -= 7
		if self.x > screen_width: 
			self.x = 0
		if self.x <= -200: 
			self.x = 900		
		print self.animal_position
		print self.x
		print screen_width
		self.animal_position = (self.x, -10)


	def draw(self):
		screen.blit(self.image, self.animal_position)	



