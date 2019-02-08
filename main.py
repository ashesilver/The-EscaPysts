#!/bin/usr/python3
# -*- coding:utf8 -*-

import pygame, time
from pygame.locals import *

from random import randint
from math import *

def initialize(screen_l = 1200,screen_h = 675):
	#returns pygame object (weird stuff)
	pygame.init()
	screen = pygame.display.set_mode((screen_l,screen_h))
	pygame.display.set_caption("Escape Game")
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
	#gives a "quit" if the player presses Alt+F4, otherwise gives the pressed keys

	keys_name = ["U","L","D","R","Enter","ENTER","esc","1","2","3","4"]
	keys_nb = [273,276,274,275,13,271,27,38,233,34,39]
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

#///////////////////////////////// execution
	
	"""if event.type == pygame.KEYDOWN:
			
			for x in range(0,len(keys_nb)):

				if event.key == keys_nb[x] and not(keys_name[x] in keys_input):
					keys_input.append(keys_name[x])

		if event.type == KEYUP:
			for x in range(0,len(keys_nb)):
				if event.key == keys_nb[x] and keys_name[x] in keys_input:
					keys_input.remove(keys_name[x])"""

#///////////////////////////////// execution

screen = initialize()

QUIT = False
while not QUIT:
	QUIT = getKeys()
	if  type(QUIT) != bool:
		#print(QUIT)
		QUIT = False