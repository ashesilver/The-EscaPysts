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

		self.size = [1,1] #ah j'en ai besoin pour graphique tu touche pas hein !
		self.imageAdress = "./images/player.jpg"


	def hidden(self,other):
		is_hidden = False
		for element in gameplayElements.var["lvl"+str(level.id).hideout.positions]:
			if element == other.position:
				is_hidden = True
		return is_hidden

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
		self.graphicHandlerObject.displayActivatable(self)