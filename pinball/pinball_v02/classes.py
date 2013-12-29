from settings import *
import pygame, sys, random
pygame.init()

class Rectangle():
	def __init__(self, x, y, width, height, color):
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def display(self):
		pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])	
		pygame.draw.rect(screen, BLACK, [self.x, self.y, self.width, self.height], 1)

