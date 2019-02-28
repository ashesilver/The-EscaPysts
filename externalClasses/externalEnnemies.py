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
		self.triggered = False
		self.graphicHandlerObject.drawCircle(self.position[0],self.position[1])
		self.direction="up"

		self.walkTick = 0

	def walk(self):
		self.walkTick += 1
		if not self.stun and not self.triggered and not self.walkTick%4: #walk activates each %x frames
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
