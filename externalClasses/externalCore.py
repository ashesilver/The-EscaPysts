#!/bin/usr/python3
#-*-coding:utf8;-*-

from externalClasses.externalGraphics import *
from externalClasses.externalLevel import *
from externalClasses.externalPlayer import *
from externalClasses.externalMenu import *

def skipInit(cls):
    actualInit = cls.__init__
    cls.__init__ = lambda *args, **kwargs: None
    instance = cls()
    cls.__init__ = actualInit
    return instance

class Core():
	"""classe prinicpale gérant toutes les autres"""

	graphicHandlerObject = Graphics(1000,1000)
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

		self.winMenuHandlerObject = Menu(self.graphicHandlerObject)
		self.winMenuHandlerObject.backgroundAdress = "images/win.png"
		self.winMenuHandlerObject.buttonCoords = [[0,0,800,800]]
		self.winMenuHandlerObject.buttonImages = ["images/win.png"]

			
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
		win = False
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
				if win :
					self.winMenuHandlerObject.update()
					if self.winMenuHandlerObject.buttonPressed[0]:
						run = False
						self.graphicHandlerObject.killWindow()
				elif "esc" in self.keys or options:

					self.optionsMenuHandlerObject.update()

					if self.optionsMenuHandlerObject.buttonPressed[0]:
						if not play :
							self.levelHandlerObject = skipInit(Level)
							self.levelHandlerObject.memoryPath()
							self.playerHandlerObject = None
						self.levelHandlerObject.id = -1
						self.levelHandlerObject.saveNext()
						play = False
						self.graphicHandlerObject.switchCursors()
						if not static :
							static = True
						self.optionsMenuHandlerObject.buttonPressed[0] = False
						self.deleteLevel()
						self.graphicHandlerObject.displayBackgroundUpdate(self.optionsMenuHandlerObject.backgroundAdress)
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
						self.mainMenuHandlerObject.buttonPressed[0] = False
						static = False
						try :
							self.startLevel()
							play = True
						except :
							self.levelHandlerObject = skipInit(Level)
							self.levelHandlerObject.id = -1
							self.levelHandlerObject.memoryPath()
							self.playerHandlerObject = skipInit(Player)
							self.playerHandlerObject.death = False
							self.playerHandlerObject.win = False
							play = False
							win = True

					if self.playerHandlerObject.death:
						self.deleteLevel()
						self.startLevel()
					elif self.playerHandlerObject.win:
						self.levelHandlerObject.saveNext()
						self.deleteLevel()
						try :
							self.startLevel()
						except :
							self.levelHandlerObject = skipInit(Level)
							self.levelHandlerObject.memoryPath()
							self.playerHandlerObject = None
							self.levelHandlerObject.id = -1
							self.levelHandlerObject.saveNext()
							self.deleteLevel()
							play = False
							win = True

					####### in-level actions :
					if play:
						self.graphicHandlerObject.displayBackgroundUpdate()
						self.playerHandlerObject.keys = self.keys[:]
						self.playerHandlerObject.update()
						self.levelHandlerObject.update(self.fpsLimit)

						#print(self.playerHandlerObject.position)
			if run :
				####### endLoop actions
				self.keysRegister = temporaryKeyLock[:]
				self.graphicHandlerObject.generalDisplayUpdate()