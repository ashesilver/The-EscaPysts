#!/bin/usr/python3
#-*-coding:utf8;-*-

from externalClasses.externalGraphics import *
from externalClasses.externalLevel import *
from externalClasses.externalPlayer import *

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
				if x != "U" and x !="D" and x !="L" and x !="R":
					self.keys.remove(x)
			else :
				if x != "U" and x !="D" and x !="L" and x !="R":
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

				####### options menu trigger
				if "esc" in self.keys or options:
					if "esc" in self.keys:
						options = not(options)
				####### level trigger
				if (("ENTER" in self.keys or "Enter" in self.keys) or play) and not options:
					if not play:
						self.levelHandlerObject = Level(self.graphicHandlerObject)
						self.playerHandlerObject = Player(self.graphicHandlerObject,self.levelHandlerObject,self.keys)
						self.ennemiesHandlerObject = Ennemies(self.graphicHandlerObject,self.levelHandlerObject,self.playerHandlerObject)
						play = True
						static = False
						# self.levelHandlerObject.test()
					self.graphicHandlerObject.backgroundUpdate()
					self.playerHandlerObject.keys = self.keys[:]
					self.ennemiesHandlerObject.walk()
					self.playerHandlerObject.move_player()

					
					####### in-level actions :
					
		
				####### main menu
				if static and not options:
					pass


				####### endLoop actions
				self.keysRegister = temporaryKeyLock[:]

				####### tests zone

				#print(self.keys)
