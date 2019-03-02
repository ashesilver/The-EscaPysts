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

		self.walkLock =[]
		self.lock()
		
		self.size = [1,1] #ah j'en ai besoin pour graphique tu touche pas hein !
		self.imageAdress = "./images/player.jpg"
		self.image = None


	def hideout(self):
		count = 0
		for element in self.levelHandlerObject.elements:
			for x in element:
				if x.position == self.position and x.hideable: #and not self.spotted
					count=1
					self.hidden = True
		if not count :
			self.hidden = False

	def lock(self):
		for y in self.levelHandlerObject.elements :
			if y[0].type=="wall" :
				x=y[:]

		for e in x :
			for xcord in range(0,e.size[0]):
				for ycord in range(0,e.size[1]):
					self.walkLock.append([xcord+e.position[0],ycord+e.position[1]])
		print(self.walkLock)

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
			if self.position in self.walkLock :
				self.position = self.positionPrec[:]

	def update(self):
		self.move_player()
		self.hideout()
		self.graphicHandlerObject.displayActivatable(self)
