#!/bin/usr/python3
# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *

def initialize(screen_l,screen_h):
	#returns pygame object (weird stuff)
	pygame.init()
	screen = pygame.display.set_mode((screen_l,screen_h), HWSURFACE | DOUBLEBUF )
	pygame.display.set_caption("The EscaPysts")
	#pygame.display.set_icon(pygame.image.load('images/'))
	pygame.display.flip()
	return screen

class Graphics():

	"""Graphic handler for all pygame graphicEvents"""

	screen = ()

	def __init__(self, screen_l = 800,screen_h = 800):
		self.screen_l = screen_l
		self.screen_h = screen_h

		Graphics.screen = initialize(self.screen_l,self.screen_h)

		self.leftClick = 0
		self.rightClick = 0

		self.buttonImage = None

		self.yellowSquare = pygame.image.load("images/sq.png").convert()
		self.yellowSquare = pygame.transform.scale(self.yellowSquare, (int(self.screen_l/60),int(self.screen_h/60)) )

	def killWindow(self):
		pygame.quit()

	#DISPLAY METHODS

	
	def displaySquare(self,coordinates):
		self.screen.blit(self.yellowSquare, [ int(x*(self.screen_h/60)) for x in coordinates])

	def displayActivatable(self,element):
		if element.image == None:
			img = pygame.image.load(element.imageAdress).convert()
			img = pygame.transform.scale(img, [ int(x*self.screen_h/60) for x in element.size] )
			element.image = img
		else :
			img = element.image
		self.screen.blit(img, [ int(x*self.screen_h/60) for x in element.position])
		
	def displayBackgroundUpdate(self,imageAdress=None):
		if not imageAdress==None:
			self.bckg = pygame.image.load(imageAdress).convert()
			self.bckg = pygame.transform.scale(self.bckg, (self.screen_l,self.screen_h))

		self.screen.blit(self.bckg,(0,0))

	def displayButton(self,imageAdress,coordinates):
		if self.buttonImage == None :
			self.buttonImage = pygame.image.load(imageAdress).convert()
			self.buttonImage = pygame.transform.scale(self.buttonImage, (int(coordinates[2]*(self.screen_l/800)),int(coordinates[3]*(self.screen_h/800))) )
		self.screen.blit(self.buttonImage, [int(coordinates[0]*(self.screen_l/800)),int(coordinates[1]*(self.screen_h/800))	])
		

	def generalDisplayUpdate(self):
		pygame.display.flip()


	#GETKEYS

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

	def getMouse(self):
		self.leftClick = pygame.mouse.get_pressed()[0]
		self.rightClick = pygame.mouse.get_pressed()[2]
		return pygame.mouse.get_pos()
