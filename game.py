import pygame
from player import *
from settings import *


class Game:
    def __init__(self):
        self.gameActive = False
        self.numberOfPlayers = 0
        self.player1 = pygame.sprite.Group()
        self.player2 = pygame.sprite.Group()

    def player1Setup(self):
        self.player1Sprite = Player(bounds, 0)
        self.player1.add(self.player1Sprite)

    def player2Setup(self):
        self.player2Sprite = Player(bounds, 1)
        self.player2.add(self.player2Sprite)

    def update(self):
    	pass