import sys
import pygame
from pygame.locals import *
from settings import *
from player import *
from game import *


pygame.init()
pygame.display.set_caption('Dungeon Hordes')
screen = pygame.display.set_mode((WIDTH,HEIGHT),RESIZABLE)
clock = pygame.time.Clock()

# initialize joysticks then print the joystick names
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
	print(joystick.get_name())

# player motion setup
player1Motion = [0, 0]
player2Motion = [0, 0]

game = Game()

def resetPlayerMotion():
	# reset motion to 0 when axis value gets too low. prevents joystick drifting.
	if game.numberOfPlayers > 0:
		if abs(player1Motion[0]) < 0.1:
			player1Motion[0] = 0
		if abs(player1Motion[1]) < 0.1:
			player1Motion[1] = 0
		game.player1Sprite.update(player1Motion) # update player 1

	if game.numberOfPlayers > 1:
		if abs(player2Motion[0]) < 0.1:
			player2Motion[0] = 0
		if abs(player2Motion[1]) < 0.1:
			player2Motion[1] = 0
		game.player2Sprite.update(player2Motion) # update player 2

def eventHandling():
	for event in pygame.event.get(): # event loop

		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		if game.gameActive == False:
			if event.type == JOYBUTTONDOWN and event.joy == 0:
				if event.button == 7:
					game.gameActive = True
					game.numberOfPlayers = 1
					game.player1Setup()
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()

		if game.gameActive:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				game.gameActive = False
				game.numberOfPlayers = 0
			elif event.type == JOYAXISMOTION: 
				if event.joy == 0: # joystick 0 axis controls player 1
					if event.axis < 2:
						player1Motion[event.axis] = event.value
				elif event.joy == 1: # joystick 1 axis controls player 2
					if event.axis < 2:
						player2Motion[event.axis] = event.value
			elif event.type == JOYBUTTONDOWN and event.joy == 1:
				if event.button == 7:
					game.numberOfPlayers = 2
					game.player2Setup()

def playerShooting():
	playerFireDirection = [[0,0],[0,0]]

	for joystick in joysticks:
		if joystick.get_button(0) and joystick.get_button(1): # buttons for shooting need to be outside the event handler to repeat fire while holding
			playerFireDirection[joystick.get_id()] = [1,1]
		elif joystick.get_button(1) and joystick.get_button(3):
			playerFireDirection[joystick.get_id()] = [1,-1]
		elif joystick.get_button(3) and joystick.get_button(2):
			playerFireDirection[joystick.get_id()] = [-1,-1]
		elif joystick.get_button(2) and joystick.get_button(0):
			playerFireDirection[joystick.get_id()] = [-1,1]
		elif joystick.get_button(0):
			playerFireDirection[joystick.get_id()] = [0,1]
		elif joystick.get_button(1):
			playerFireDirection[joystick.get_id()] = [1,0]
		elif joystick.get_button(3):
			playerFireDirection[joystick.get_id()] = [0,-1]
		elif joystick.get_button(2):
			playerFireDirection[joystick.get_id()] = [-1,0]

		if game.numberOfPlayers > 0:
			if playerFireDirection[0] != [0,0]:
				game.player1Sprite.shoot(playerFireDirection[0])
		
		if game.numberOfPlayers > 1:
			if playerFireDirection[1] != [0,0]:
				game.player2Sprite.shoot(playerFireDirection[1])



# main loop
while True:
	screen.fill('black')

	if game.gameActive == False:
		screen.fill('red')

	if game.gameActive:
		if game.numberOfPlayers > 0:
			game.player1.draw(screen)
			game.player1Sprite.arrows.draw(screen)
		if game.numberOfPlayers > 1:
			game.player2.draw(screen)
			game.player2Sprite.arrows.draw(screen)

		resetPlayerMotion()	
		playerShooting()

		game.update()

	eventHandling()
	pygame.display.update()
	clock.tick(FPS)
