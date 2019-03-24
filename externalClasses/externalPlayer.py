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
		self.walkTick = 0
		self.hidden = False

		self.walkLock =[]
		self.keysList = []
		self.hideouts = []
		self.lock()
		
		self.size = [1,1] #ah j'en ai besoin pour graphique tu touche pas hein !
		self.imageAdress = "./images/player.jpg"
		self.image = None
		self.death = False
		self.win = False

	def hideout(self):
		count = 0
		for x in self.hideouts :
			if x.position == self.position: #and not self.spotted
				if not self.hidden :
					self.walkTick = -20
				count=1
				self.hidden = True
		if not count :
			self.hidden = False

	def lock(self):
		for y in self.levelHandlerObject.elements :
			if y[0].type=="wall" :
				x=y[:]
			elif y[0].hideable :
				self.hideouts=y[:]
			elif y[0].type=='gate' :
				self.endGate = y[0] 
			elif y[0].type=='key' :
				self.keysList = y

		for e in x :
			for xcord in range(0,e.size[0]):
				for ycord in range(0,e.size[1]):
					self.walkLock.append([xcord+e.position[0],ycord+e.position[1]])

	def move_player(self):
		self.walkTick += 1
		if not self.walkTick%5 and self.walkTick>0 :
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
			self.walkTick = 0

	def update(self):
		self.move_player()
		self.hideout()
		self.graphicHandlerObject.displayActivatable(self)
		if self.position == self.endGate.position and self.endGate.open:
			self.win = True

		for x in self.keysList :
			if x.position == self.position :
				x.picked = True
				self.keysList.remove(x)
		if len(self.keysList) == 0 :
			self.endGate.open = True
