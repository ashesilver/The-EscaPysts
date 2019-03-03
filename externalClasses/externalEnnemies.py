#!/bin/usr/python3
# -*- coding:utf-8 -*-

import externalClasses.data.EnnemiesPattern as ennemiesPat

class Ennemies():
	def __init__(self, arg, levelO, player0):
		self.graphicHandlerObject = arg
		self.levelHandlerObject = levelO
		self.playerHandlerObject = player0
		self.position = [20,15]
		self.positionPrec= [0,0]
		self.stun = False
		self.direction = "up"
		self.vision = [[0][0]]
		self.size = [1,1] #ah j'en ai besoin pour graphique tu touche pas hein !
		self.imageAdress = "./images/ennemy.jpg"
		self.image = None
		self.walkTick = 0
		self.vision = [[],[]]

	def walk(self):
		self.walkTick += 1
		if not self.stun and not self.walkTick%6: #walk activates each %x frames
			self.positionPrec = self.position[:]
			if self.position[0]==20 and self.position[1]!=6: #up
				self.direction = "up"  
				self.position[1]-=1
				self.vision = [[],[]]
				for i in range(5):
					self.vision[1].append(self.position[1]-i)

			elif self.position[0]!=32 and self.position[1]==6: #right
				self.direction = "right" 
				self.position[0]+=1
				self.vision = [[],[]]
				for i in range(5):
					self.vision[0].append(self.position[0]+i)

			elif self.position[0]==32 and self.position[1]!=20: #down
				self.direction = "down" 
				self.position[1]+=1
				self.vision = [[],[]]
				for i in range(5):
					self.vision[1].append(self.position[1]+i)

			elif self.position[1]==20 and self.position[0]!=15: #left
				self.direction = "left" 
				self.position[0]-=1
				self.vision = [[],[]]
				for i in range(5):
					self.vision[0].append(self.position[0]-i)
			self.walkTick = 0

	def followPlayer(self,other):
		if self.playerHandlerObject.position[0] in self.vision[0] or self.playerHandlerObject.position[1] in self.vision[1]:
				self.graphicHandlerObject.killWindow()
		#if not self.stun and not self.playerHandlerObject.hidden:
		#	print("lalalalala")
			

	def search(self,other):
		if not self.stun and self.playerHandlerObject.hidden: #and other.hidden
			pass

	def update(self):
		self.walk()
		self.graphicHandlerObject.displayActivatable(self)
