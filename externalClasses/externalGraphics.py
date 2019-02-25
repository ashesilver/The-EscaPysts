#!/bin/usr/python3
# -*- coding:utf-8 -*-

import pygame
from random import randint

def initialize(screen_l,screen_h):
	#returns pygame object (weird stuff)
	pygame.init()
	screen = pygame.display.set_mode((screen_l,screen_h))
	pygame.display.set_caption("The EscaPysts")
	#pygame.display.set_icon(pygame.image.load('images/'))
	pygame.display.flip()
	return screen

class Graphics():
	"""Graphic handler for all pygame graphicEvents"""

	screen = ()

	def __init__(self, screen_l = 1066,screen_h = 800):
		self.screen_l = screen_l
		self.screen_h = screen_h

		Graphics.screen = initialize(self.screen_l,self.screen_h)

	def levelBackroundUpdate(self,imageAdress):
		bckg = pygame.image.load(imageAdress).convert()
		self.screen.blit(bckg,(0,0))
		pygame.display.flip()

	def killWindow(self):
		pygame.quit()

	"""
	def drawGrid(self):
		for x in range(1,40):
			pygame.draw.line(self.screen,[255,255,255],(x*self.screen_l/40,0),(x*self.screen_l/40,self.screen_h))
		for y in range(1,30):
			pygame.draw.line(self.screen,[255,255,255],(0,y*self.screen_h/30),(self.screen_l,y*self.screen_h/30))
		pygame.display.flip()"""

	def drawCircle(self,x,y):
		pygame.draw.circle(self.screen,[randint(0,255),randint(0,255),randint(0,255)],[int(x*self.screen_l/(40*2)+5),int(y*self.screen_h/(30*2)+5)],4,0)
		pygame.display.flip()

	def destroyCircle(self,x,y):
		pygame.draw.circle(self.screen,[0,0,0],[int(x*self.screen_l/(40*2)+5),int(y*self.screen_h/(30*2)+5)],4,0)
		pygame.display.flip()

	def drawActivatable(element):
			img = pygame.image.load(element.imageAdress).convert()
			#img_rect = img.get_rect()
			screen.blit(img,element.position)

	def getKeys(self):
		#no parameters
		#gives a "quit = true" if the player presses Alt+F4, otherwise gives the pressed keys

		keys_name = ["U","L","D","R","Enter","ENTER","esc","1","2","3","4"]
		keys_nb = [273,276,274,275,13,271,27,38,233,34,39] # touches "1234" pour linux : [38,233,34,39] - alternative windows [49,50,51,52]
		keys_input = []

		all_keys = pygame.key.get_pressed()
		if all_keys[pygame.K_F4] and (all_keys[pygame.K_LALT] or all_keys[pygame.K_RALT]): 
			self.killWindow()
			return(True)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.killWindow()
				return(True)
		for k in keys_nb:
			if all_keys[k] :
				keys_input.append(keys_name[keys_nb.index(k)])
		#print(all_keys.index(1))
		
		return keys_input