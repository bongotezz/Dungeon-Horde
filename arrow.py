import pygame
from os import path
from settings import *

class Arrow(pygame.sprite.Sprite):
	def __init__(self, location, direction):
		super().__init__()
		self.location = location
		self.direction = direction
		self.speed = 12

		self.image = pygame.image.load("Assets/Images/arrow.png").convert_alpha()

		if self.direction == [1,0]:
			pass # the arrow image is by default this orientation 0 degrees
		elif self.direction == [1,-1]:
			self.image = pygame.transform.rotate(self.image, 45)
		elif self.direction == [0,-1]:
			self.image = pygame.transform.rotate(self.image, 90)
		elif self.direction == [-1,-1]:
			self.image = pygame.transform.rotate(self.image, 135)
		elif self.direction == [-1,0]:
			self.image = pygame.transform.rotate(self.image, 180)
		elif self.direction == [-1,1]:
			self.image = pygame.transform.rotate(self.image, 225)
		elif self.direction == [0,1]:
			self.image = pygame.transform.rotate(self.image, 270)
		elif self.direction == [1,1]:
			self.image = pygame.transform.rotate(self.image, 315)

		self.rect = self.image.get_rect(center = location)


	def update(self):
		self.rect.centerx += self.direction[0] * self.speed
		self.rect.centery += self.direction[1] * self.speed

		if self.rect.centerx > WIDTH or self.rect.centerx < 0 or self.rect.centery > HEIGHT or self.rect.centery < 0:
			self.kill()