#!/bin/usr/python3
#-*-coding:utf8;-*-

from externalClasses.externalGraphics import *
from externalClasses.externalLevel import *
from externalClasses.externalPlayer import *
from externalClasses.externalMenu import *

class Core():
	"""classe prinicpale gérant toutes les autres"""

	graphicHandlerObject = Graphics(600,600)
	clock = pygame.time.Clock()
	
	def __init__(self, FPS_limit=240):
		self.fpsLimit = FPS_limit
		self.quit = False

		self.mainMenuHandlerObject = Menu(self.graphicHandlerObject)

		self.optionsMenuHandlerObject = Menu(self.graphicHandlerObject)
		self.optionsMenuHandlerObject.buttonPressed = [0,0]
		self.optionsMenuHandlerObject.buttonCoords = [[155,490,495,97],[62,663,676,80]]
		self.optionsMenuHandlerObject.buttonImages = ["images/opbut_1.png","images/opbut_2.png"]
		self.optionsMenuHandlerObject.backgroundAdress = "images/options.png"

			
	def keyLock(self):
		for x in self.keys:
			if x in self.keysRegister:
				if x != "U" and x !="D" and x !="L" and x !="R":
					self.keys.remove(x)
			else :
				if x != "U" and x !="D" and x !="L" and x !="R":
					self.keysRegister.append(x)
				
	def startLevel(self):
		self.graphicHandlerObject.switchCursors()
		self.graphicHandlerObject.displayLoadingScreen()
		self.levelHandlerObject = Level(self.graphicHandlerObject)
		self.playerHandlerObject = Player(self.graphicHandlerObject,self.levelHandlerObject,self.keys)
		for x in self.levelHandlerObject.ennemies :
			x.playerHandlerObject = self.playerHandlerObject
		self.levelHandlerObject.playerHandlerObject = self.playerHandlerObject
		self.mainMenuHandlerObject.buttonPressed[0] = False

	def deleteLevel(self):
		self.graphicHandlerObject.switchCursors()
		del self.levelHandlerObject
		del self.playerHandlerObject

	def run(self):

		run = True
		static = True #(menu)

		options = False
		play = False

		####### game loop
		while run:
			Core.clock.tick(self.fpsLimit) #defines clock's max speed by (1/FPS_limit) ms per frame
			self.keys = self.graphicHandlerObject.getKeys()

			####### game-ender
			if type(self.keys) == bool:
				run = not(self.keys)
				self.keys = []
			else :
				temporaryKeyLock = self.keys[:]
		
			if run :
				self.keyLock()
			
				####### options menu trigger
				if "esc" in self.keys or options:

					self.optionsMenuHandlerObject.update()

					if self.optionsMenuHandlerObject.buttonPressed[0]:
						if not play :
							self.levelHandlerObject = Level(self.graphicHandlerObject)
							self.playerHandlerObject = None
						self.levelHandlerObject.id = -1
						self.levelHandlerObject.saveNext()
						play = False
						if static :
							self.graphicHandlerObject.switchCursors()
						else :
							static = True
						self.optionsMenuHandlerObject.buttonPressed[0] = False
						self.deleteLevel()
						self.graphicHandlerObject.displayBackgroundUpdate(self.optionsMenuHandlerObject.backgroundAdress, False)
					elif self.optionsMenuHandlerObject.buttonPressed[1]:
						run = False
						self.graphicHandlerObject.killWindow()

					if "esc" in self.keys:
						if options and play:
							self.graphicHandlerObject.displayBackgroundUpdate(self.levelHandlerObject.imageAdress)
							self.graphicHandlerObject.switchCursors()
						elif play :
							self.graphicHandlerObject.switchCursors()
						options = not(options)


				####### main menu
				elif static:
					self.mainMenuHandlerObject.update()

				####### level trigger
				if (("ENTER" in self.keys or "Enter" in self.keys or self.mainMenuHandlerObject.buttonPressed[0]) or play) and not options:
					if not play:
						self.startLevel()
						play = True
						static = False
						# self.levelHandlerObject.test()
					if self.playerHandlerObject.death:
						self.deleteLevel()
						self.startLevel()
					elif self.playerHandlerObject.win:
						self.levelHandlerObject.saveNext()
						self.deleteLevel()
						self.startLevel()
					####### in-level actions :
					self.graphicHandlerObject.displayBackgroundUpdate()
					self.playerHandlerObject.keys = self.keys[:]
					self.playerHandlerObject.update()
					self.levelHandlerObject.update(self.fpsLimit)

						#print(self.playerHandlerObject.position)
			if run :
				####### endLoop actions
				self.keysRegister = temporaryKeyLock[:]
				self.graphicHandlerObject.generalDisplayUpdate()
		
		####### tests zone
				
