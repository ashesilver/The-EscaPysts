#!/bin/usr/python3
# -*- coding:utf-8 -*-

import pygame, time, copy
from pygame.locals import *

from random import randint
from math import *

###### external files
import gridElements as gameplayElements
import EnnemiesPattern as ennemiesPat

def initialize(screen_l = 1200,screen_h = 675):
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

	def drawGrid(self):
		for x in range(1,40):
			pygame.draw.line(self.screen,[255,255,255],(x*self.screen_l/40,0),(x*self.screen_l/40,self.screen_h))
		for y in range(1,30):
			pygame.draw.line(self.screen,[255,255,255],(0,y*self.screen_h/30),(self.screen_l,y*self.screen_h/30))
		pygame.display.flip()

	def drawCircle(self,x,y):
		pygame.draw.circle(self.screen,[randint(0,255),randint(0,255),randint(0,255)],[x*self.screen_l/40+10,y*self.screen_h/30+10],8,0)
		pygame.display.flip()

	def destroyCircle(self,x,y):
		pygame.draw.circle(self.screen,[0,0,0],[x*self.screen_l/40+10,y*self.screen_h/30+10],8,0)
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
		

class Core():
	"""classe prinicpale gérant toutes les autres"""

	graphicHandlerObject = Graphics(800,600)
	clock = pygame.time.Clock()
	
	def __init__(self, FPS_limit=240):
		self.fpsLimit = FPS_limit
		self.quit = False

	"""
	def playableInLoop(self):
		run = True
		while run:
			if type(self.keys) == bool:
				self.quit = True
			run = not(self.quit)
	"""
			
	def keyLock(self):
		for x in self.keys:
			if x in self.keysRegister:
				self.keys.remove(x)
			else :
				self.keysRegister.append(x)
				


	def run(self):

		run = True
		static = True #(menu)

		options = False
		play = False

		####### game loop
		while run:
			Core.clock.tick(self.fpsLimit) #defines clock's max speed by (1/FPS_limit) ms per frame
			self.keys = self.graphicHandlerObject.getKeys()

			#temporaryKeyLock = copy.deepcopy(self.keys)
			try :
				temporaryKeyLock = self.keys[:]
				self.keyLock()
			
			except :
				####### game-ender
				if type(self.keys) == bool:
					run = not(self.keys)

			else :
				####### level trigger
				if (("ENTER" or "Enter") in self.keys or play):
					if not play:
						self.levelHandlerObject = Level(self.graphicHandlerObject)
						self.playerHandlerObject = Player(self.graphicHandlerObject,self.levelHandlerObject,self.keys)
						self.ennemiesHandlerObject = Ennemies(self.graphicHandlerObject,self.levelHandlerObject,self.playerHandlerObject)
						play = True
						static = False
						# self.levelHandlerObject.test()
					self.ennemiesHandlerObject.walk()
					#self.playerHandlerObject.move_player()

						

					"""
					x = self.memoryPath()
					if not(bool(x)):
						self.levelHandlerObject = Level(int(x))
					else :
						self.levelHandlerObject = Level()
					"""


					####### in-level actions :


				####### options menu trigger
				if "esc" in self.keys or options:
					if "esc" in self.keys:
						options = not(options)
					static = False
				
				####### main menu
				if static:
					pass


				####### endLoop actions
				self.keysRegister = temporaryKeyLock[:]

				####### tests zone

				#print(self.keys)



class Level():
	"""Level : gestionnaire du niveau en cours"""

	def __init__(self, arg=None):
		self.memoryPath()
		self.id = int(self.save)

		self.selector = {}
		self.locator = []

		tmp = gameplayElements.var["lvl"+str(self.id)]
		self.elements = [ ( Activatable(x,tmp[x]['position'][i],tmp[x]['destination'][i]) for i in range(0,len(tmp[x]['position'])) ) for x in tmp ] #stores in 1 attribute/self.gridElements/ all grid elements in gridElements.py (external file)
		self.graphicHandlerObject = arg
		self.defineGrid()

	def memoryPath(self):
		self.savefile = "save.txt"

		try :
			fichier = open(self.savefile,"r")
		except:
			fichier = open(self.savefile,"w")
			fichier.write("0")
			fichier.close()
			fichier = open(self.savefile,"r")
		finally:
			self.save = int(fichier.read())
			fichier.close()

	def save(self):
		self.id += 1
		fichier = open(self.savefile,"w")
		fichier.write(str(self.id))
		fichier.close()

	def test(self):
		print(self.grid)

	def defineGrid(self):
		self.grid = [ [y for y in range (0,40)] for x in range (0,30) ]
		self.graphicHandlerObject.drawGrid()


class Activatable():
	"""Activatable  : classe des objets du niveau"""
	def __init__(self, obj, position, destination):
		self.imageAdress = obj['image']
		self.size = obj['size']
		self.position = position
		self.destination = destination



class Player():
	"""Player handler class & methods"""
	def __init__(self, graphicHandlerObject,lvl, keys):
		self.keys = keys
		self.graphicHandlerObject = graphicHandlerObject
		self.levelHandlerObject = lvl
		self.position = [10,20]
		self.graphicHandlerObject.drawCircle(self.position[0],self.position[1])


	def hidden(self,other):
		is_hidden = False
		for element in gameplayElements.var["lvl"+str(level.id).hideout.positions]:
			if element == other.position:
				is_hidden = True
		return is_hidden

	def move_player():
		

class Ennemies():
	def __init__(self, arg, levelO, player0):
		self.graphicHandlerObject = arg
		self.levelHandlerObject = levelO
		self.playerHandlerObject = player0
		self.position = [20,15]
		self.positionPrec= [0,0]
		self.stun = False
		self.triggered = False
		self.graphicHandlerObject.drawCircle(self.position[0],self.position[1])
		self.direction="up"
		# self.playerObject =

	def walk(self):
		if not self.stun and not self.triggered:
			self.positionPrec = self.position[:]
			if self.position[0]==20 and self.position[1]!=6:
				self.position[1]-=1
			elif self.position[0]!=32 and self.position[1]==6:
				self.position[0]+=1
			elif self.position[0]==32 and self.position[1]!=20:
				self.position[1]+=1
			elif self.position[1]==20 and self.position[0]!=15:
				self.position[0]-=1
			self.graphicHandlerObject.drawCircle(self.position[0],self.position[1])
			self.graphicHandlerObject.destroyCircle(self.positionPrec[0],self.positionPrec[1])

	def followPlayer(self,other):
		if not self.stun and self.triggered:
			pass

		
	def search(self,other):
		if not self.stun and self.triggered : #and other.hidden
			pass
		


#///////////////////////////////// execution


game = Core(10)
game.run()
quit()
