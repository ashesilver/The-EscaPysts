#!/bin/usr/python3
# -*- coding:utf-8 -*-

class Player():
	"""Player handler class & methods"""
	def __init__(self, graphicHandlerObject,lvl, keys):
		self.keys = keys
		self.graphicHandlerObject = graphicHandlerObject
		self.levelHandlerObject = lvl
		self.position = [10,20]
		self.positionPrec = []
		self.graphicHandlerObject.drawCircle(self.position[0],self.position[1])
		self.walkTick = 0
		self.hidden = False

		self.size = [1,1] #ah j'en ai besoin pour graphique tu touche pas hein !
		self.imageAdress = "./images/player.jpg"


	def hideout(self):
		count = 0
		for element in self.levelHandlerObject.elements:
			if element[0].position == self.position and element[0].hideable: #and not self.spotted
				count=1
				self.hidden = True
		if not count :
			self.hidden = False


	def move_player(self):
		self.walkTick += 1
		if not self.walkTick%4 :
			self.positionPrec = self.position[:]
			if "U" in self.keys and self.position[1] > 0 :
				self.position[1] -= 1
			elif "D" in self.keys and self.position[1] < len(self.levelHandlerObject.grid)-1:
				self.position[1] += 1
			if "R" in self.keys and self.position[0] < len(self.levelHandlerObject.grid[0])-1 :
				self.position[0] +=1
			elif "L" in self.keys and self.position[0] > 0:
				self.position[0] -=1

	def update(self):
		self.move_player()
		self.hideout()
		self.graphicHandlerObject.displayActivatable(self)
