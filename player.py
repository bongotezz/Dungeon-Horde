import pygame
from os import path

class Player(pygame.sprite.Sprite):
    def __init__(self, bounds, playerNumber):
    	super().__init__()
    	self.bounds = bounds
    	self.playerNumber = playerNumber

        # determine the player number and load the correct graphic
    	if self.playerNumber == 0:
    		self.image = pygame.image.load("Assets/Images/player1.jpg").convert_alpha()
    	elif self.playerNumber == 1:
    		self.image = pygame.image.load("Assets/Images/player2.jpg").convert_alpha()
    	else:
    		self.image = pygame.image.load("Assets/Images/player1.jpg").convert_alpha()

    	self.rect = self.image.get_rect()
    	self.speed = 8
    	self.rect.centerx = self.bounds[0] / 2 #width
    	self.rect.centery = self.bounds[1] / 2 #height

    def movePlayer(self,direction):  	
    	self.rect.centerx += direction[0] * self.speed
    	self.rect.centery += direction[1] * self.speed	

    def shoot(self, angle):
        pass


    def update(self, direction):
    	self.movePlayer(direction)

