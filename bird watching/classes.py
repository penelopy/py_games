from settings import *
import pygame, sys, random, math
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
		# this module makes the pupil move in a circle around the eye, to follow the bird

		# food.rect should be the bird to follow
		# eye_x an eye_y are the center of the eye

		# test code for eye following
		# ------------------------------------------------------------------------------------
		# the pupil should line at a fixed distance from the eye center, along the imaginary line that joins the eye center and the bird.
		# step 1: find the slope of the line connecting the eye and the bird
		# step 2: the following parameters are known: (distance from eye center to pupil, slope of line between eye center and pupil)
		# step 3: use this information to find and x and y position for the pupil where these parameters are also true

		# pygame.draw.line(screen, BLACK, (self.bird.x + 50, self.bird.y + 100), (self.eye_x, self.eye_y))
		x_distance = (self.bird.x - self.eye_x)
		# if x distance = 0, change it to a very small number so you don't get a "divide by 0" error
		if x_distance == 0:
			x_distance = 0.00000001
		y_distance = (self.bird.y - self.eye_y)

		# # if slope distance = 0, change it to a very small number so you don't get a "divide by 0" error
		slope = y_distance/x_distance
		if slope == 0:
			slope = 0.00000001

		# # use a trial and error method to find a new x and y, to find the correct z
		# # when you have find the correct z, the x and y are correct
		# # you use the slope of the angle between the eye and the bird
		z = 0
		y = 0.1
		y_increment = 0.1
		while z <= 12:
			y += y_increment
			x = y/slope
			z = math.sqrt(x*x + y*y)
		# correct for quadrant issues
		if y_distance < 0:
			x *= -1
			y *= -1

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



