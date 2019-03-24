#!/bin/usr/python3
#-*-coding:utf8;-*-

class Menu():
	"""docstring for Menu"""
	def __init__(self, arg):
		self.backgroundAdress = "images/menu.png"
		self.graphicHandlerObject = arg

		#self.graphicHandlerObject.displayBackgroundUpdate(self.backgroundAdress)

		self.buttonCoords = [[245,210,295,425]]  #j'aurais pu faire une classe 'bouton' mais hé... on en a qu'un seul, ça va oui ?
		self.buttonPressed = [0]
		self.buttonImages = ["images/bouton_menu.png"]

	def update(self):
		self.graphicHandlerObject.displayBackgroundUpdate(self.backgroundAdress)
		self.mousePos = self.graphicHandlerObject.getMouse()
		self.UI_button()

	def UI_button(self):
		for x in self.buttonCoords:
			if ((x[0])*(self.graphicHandlerObject.screen_l/800)<self.mousePos[0]<(x[0]+x[2])*(self.graphicHandlerObject.screen_l/800)) and ((x[1])*(self.graphicHandlerObject.screen_l/800)<self.mousePos[1]<(x[1]+x[3])*(self.graphicHandlerObject.screen_l/800)):
				self.graphicHandlerObject.displayButton(self.buttonImages[self.buttonCoords.index(x)],x)
				if self.graphicHandlerObject.leftClick :
					self.buttonPressed[self.buttonCoords.index(x)] = True
		


# reset : [154,489,495,97],"images/opbut_1.png"