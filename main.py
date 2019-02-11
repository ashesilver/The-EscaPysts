#!/bin/usr/python3
# -*- coding:utf-8 -*-

import pygame, time
from pygame.locals import *

from random import randint
from math import *

import gridElements

def initialize(screen_l = 1200,screen_h = 675):
	#returns pygame object (weird stuff)
	pygame.init()
	screen = pygame.display.set_mode((screen_l,screen_h))
	pygame.display.set_caption("The EscaPysts")
	#pygame.display.set_icon(pygame.image.load('images/'))
	pygame.display.flip()
	return screen

def getData(classe,i=0,sort=None):
	"""get the data of something;
	i must be an int ; sort must be a str ; classe must be an existing object"""
	obj = classe
	obj.number = i
	obj.kind = sort
	return obj.output_data()

def getKeys():
	#no parameters
	#gives a "quit = true" if the player presses Alt+F4, otherwise gives the pressed keys

	keys_name = ["U","L","D","R","Enter","ENTER","esc","1","2","3","4"]
	keys_nb = [273,276,274,275,13,271,27,49,50,51,52] # touches "1234" pour linux : [38,233,34,39] - alternative windows [49,50,51,52]
	keys_input = []

	all_keys = pygame.key.get_pressed()
	if all_keys[pygame.K_F4] and (all_keys[pygame.K_LALT] or all_keys[pygame.K_RALT]): 
		return(True)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return(True)
	for k in keys_nb:
		if all_keys[k] :
			keys_input.append(keys_name[keys_nb.index(k)])
	#print(all_keys.index(1))
	
	return keys_input



class Graphics():
	"""Graphic handler for all pygame graphicEvents"""

	screen = initialize()

	def __init__(self, arg=None):
		self.arg = arg

	def levelBackroundUpdate(self,imageAdress):
		bckg = pygame.image.load(imageAdress).convert()
		self.screen.blit(bckg,(0,0))
		pygame.display.flip()

	def killWindow(self):
		pygame.quit()
		

class Core():
	"""classe prinicpale gérant toutes les autres"""

	graphicHandler = Graphics()
	clock = pygame.time.Clock()
	
	def __init__(self, FPS_limit=240):
		self.fpsLimit = FPS_limit
		self.quit = False


		self.temporaryKeyLock = []

	def playableInLoop(self):
		run = True
		while run:


			if type(self.keys) == bool:
				self.quit = True
			run = not(self.quit)
			
	def keyLock(self):
		for x in self.keys:
			if x in self.keysRegister:
				self.keys.remove(x)
				


	def run(self):

		run = True
		static = True

		options = False
		play = False

		while run:
			Core.clock.tick(self.fpsLimit) #defines clock's max speed by (1/FPS_limit) ms per frame
			self.keys = getKeys()
			self.temporaryKeyLock = self.keys

			####### first level trigger
			if (("ENTER" or "Enter") in self.keys or play) and not options:
				play = True
				static = False
				self.levelHandler = Level()
				self.playerHandler = Player(self.keys)

			####### options menu trigger
			if "esc" in self.keys or options:
				options = True
				static = False

			if static:
				pass


			####### game-ender
			if type(self.keys) == bool:
				self.quit = True
			run = not(self.quit)


class Level():
	"""Level : gestionnaire du niveau en cours"""

	count = 0

	def __init__(self, arg=None):
		self.arg = arg
		self.id = Level.count

		self.gridSelector = {}
		self.gridLocator = []
		self.gridElements = [ Activatable(x) for x in gridElements.var["lvl"+str(self.id)] ] #stores in 1 attribute/self.gridElements/ all grid elements in gridElements.py (external file)



		Level.count+=1


class Activatable():
	"""Activatable  : classe des objets du niveau"""
	def __init__(self, arg=None):
		self.arg = arg

class Player():
	"""Player handler class & methods"""
	def __init__(self, keys):
		self.keys = keys
		

		
		


#///////////////////////////////// execution

game = Core(60)
game.run()
print(test.gridElements[0])