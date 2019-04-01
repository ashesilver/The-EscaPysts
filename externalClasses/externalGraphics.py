#!/bin/usr/python3
# -*- coding:utf-8 -*-

import os,warnings
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

		if os.name == "posix" :
			self.keys_nb = [273,276,274,275,13,271,27,38,233,34,39]
		elif os.name == "nt" :
			self.keys_nb = [273,276,274,275,13,271,27,49,50,51,52]
		else :
			warnings.warn(os.name+" OS ins't supported for The EscaPysts !",Warning)
			self.keys_nb = []
		self.keys_name = ["U","L","D","R","Enter","ENTER","esc","1","2","3","4"]

		self.leftClick = 0
		self.rightClick = 0

		self.buttonImage = None
		self.buttonAdress = ""

		self.normalCursor = pygame.mouse.get_cursor()
		self.cursorState = True

		self.yellowSquare = pygame.image.load("images/sq.png").convert()
		self.yellowSquare = pygame.transform.scale(self.yellowSquare, (int(self.screen_l/60),int(self.screen_h/60)) )
		self.lvledoverride1 = pygame.image.load("images/wall.png").convert()
		self.lvledoverride1 = pygame.transform.scale(self.lvledoverride1, (int(self.screen_l/60),int(self.screen_h/60)) )
		self.lvledoverride2 = pygame.image.load("images/ennemy.jpg").convert()
		self.lvledoverride2 = pygame.transform.scale(self.lvledoverride2, (int(self.screen_l/60),int(self.screen_h/60)) )

	def killWindow(self):
		pygame.quit()

	#DISPLAY METHODS

	
	def displaySquare(self,coordinates,override=None):
		if override==1:
			self.screen.blit(self.lvledoverride1, [ int(x*(self.screen_h/60)) for x in coordinates])
		elif override==2:
			self.screen.blit(self.lvledoverride2, [ int(x*(self.screen_h/60)) for x in coordinates])
		else :
			self.screen.blit(self.yellowSquare, [ int(x*(self.screen_h/60)) for x in coordinates])

	def displayActivatable(self,element,displaySet=True):
		if element.image == None:
			img = pygame.image.load(element.imageAdress).convert()
			img = pygame.transform.scale(img, [ int(x*self.screen_h/60) for x in element.size] )
			element.image = img
		else :
			img = element.image
		if displaySet :
			self.screen.blit(img, [ int(x*self.screen_h/60) for x in element.position])
		
	def displayBackgroundUpdate(self,imageAdress=None,do_blit=True):
		if not imageAdress==None:
			self.bckg = pygame.image.load(imageAdress).convert()
			self.bckg = pygame.transform.scale(self.bckg, (self.screen_l,self.screen_h))
		if do_blit :
			self.screen.blit(self.bckg,(0,0))

	def displayButton(self,imageAdress,coordinates):
		if self.buttonImage == None or imageAdress != self.buttonAdress:
			self.buttonAdress = imageAdress
			self.buttonImage = pygame.image.load(imageAdress).convert()
			self.buttonImage = pygame.transform.scale(self.buttonImage, (int(coordinates[2]*(self.screen_l/800)),int(coordinates[3]*(self.screen_h/800))) )
		self.screen.blit(self.buttonImage, [int(coordinates[0]*(self.screen_l/800)),int(coordinates[1]*(self.screen_h/800))	])
	
	def displayLoadingScreen(self):
		img = pygame.image.load("images/loading.png").convert()
		img = pygame.transform.scale(img, (self.screen_l,self.screen_h))
		self.screen.blit(img,(0,0))
		self.generalDisplayUpdate()

	def generalDisplayUpdate(self):
		pygame.display.flip()

	def switchCursors(self):
		if self.cursorState :
			pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
		else :
			pygame.mouse.set_cursor(*self.normalCursor)
		self.cursorState = not( self.cursorState )

	#GETKEYS/MOUSE

	def getKeys(self):
		#no parameters
		#gives a "quit = true" if the player presses Alt+F4, otherwise gives the pressed keys

		keys_input = []

		all_keys = pygame.key.get_pressed()
		if all_keys[pygame.K_F4] and (all_keys[pygame.K_LALT] or all_keys[pygame.K_RALT]): 
			self.killWindow()
			return(True)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.killWindow()
				return(True)
		for k in self.keys_nb:
			if all_keys[k] :
				keys_input.append(self.keys_name[self.keys_nb.index(k)])
		#print(all_keys.index(1))
		
		return keys_input

	def getMouse(self):
		self.leftClick = pygame.mouse.get_pressed()[0]
		self.rightClick = pygame.mouse.get_pressed()[2]
		return pygame.mouse.get_pos()

	def staticImage(self,Adr,size):
		img = pygame.image.load(Adr).convert()
		img = pygame.transform.scale(img, [ int(x*self.screen_h/60) for x in size] )
		return img

	##### obsolete

	def drawGrid(self):  #for level_editor.py
		for x in range(1,61):
			pygame.draw.line(self.screen,[125,125,125],(x*self.screen_l/60,0),(x*self.screen_l/60,self.screen_h))
		for y in range(1,61):
			pygame.draw.line(self.screen,[125,125,125],(0,y*self.screen_h/60),(self.screen_l,y*self.screen_h/60))
