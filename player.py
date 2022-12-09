import pygame
from os import path
from arrow import Arrow

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

        # arrow sprite group. arrows shot by the player
        self.arrows = pygame.sprite.Group()

        # shooting timer
        self.shootDelay = 200 # delay in ticks for firing arrows
        self.lastShot = pygame.time.get_ticks() # the last time a arrow was fired
        self.ready = True

        self.maxHP = 100
        self.currentHP = 100


    def movePlayer(self,direction):  	
    	self.rect.centerx += direction[0] * self.speed
    	self.rect.centery += direction[1] * self.speed	

    def shoot(self, angle):
        if self.ready:
            arrow = Arrow(self.rect.center,angle)
            self.arrows.add(arrow)
            self.ready = False

    def checkReadyFire(self):
        if self.ready == False:
            currentTime = pygame.time.get_ticks()
            if currentTime - self.lastShot >= self.shootDelay:
                self.ready = True
                self.lastShot = pygame.time.get_ticks()

    def update(self, direction):
        self.movePlayer(direction)
        self.arrows.update()
        self.checkReadyFire()

