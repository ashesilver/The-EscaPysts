#!/bin/usr/python3
# -*- coding:utf-8 -*-

import pygame, time
from pygame.locals import *

from random import randint
from math import *

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


class Core():
	"""classe prinicpale gérant toutes les autres"""
	def __init__(self, FPS_limit=240):
		#whole pygame support
		Core.screen = initialize()
		Core.clock = pygame.time.Clock()
		Core.FPS_limit = FPS_limit

		#object-precised vars
		self.QUIT = False

	def run(self):
		while not self.QUIT:
			Core.clock.tick(Core.FPS_limit) #defines clock's max speed by (1/FPS_limit) ms per frame
			self.QUIT = getKeys()
			if type(self.QUIT) != bool:
				print(self.QUIT)
				self.QUIT = False


#///////////////////////////////// execution

game = Core(60)
game.run()