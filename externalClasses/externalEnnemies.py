#!/bin/usr/python3
# -*- coding:utf-8 -*-

from random import *

class Ennemies():
	def __init__(self, arg, levelO, player0, pattern):
		self.graphicHandlerObject = arg
		self.levelHandlerObject = levelO
		self.playerHandlerObject = player0

		self.pattern = pattern
		self.position = self.pattern[0][0]
		self.positionPrec= [0,0]
		self.stun = False
		self.direction = "up"
		self.vision = [
			[self.position[0],self.position[1]-1],
			[self.position[0],self.position[1]-2],
			[self.position[0],self.position[1]-3],
			[self.position[0],self.position[1]-4],
			[self.position[0],self.position[1]-5],
			[self.position[0]+1,self.position[1]-4],
			[self.position[0]+1,self.position[1]-5],
			[self.position[0]-1,self.position[1]-4],
			[self.position[0]-1,self.position[1]-5]]
		self.size = [1,1] #ah j'en ai besoin pour graphique tu touche pas hein !
		self.imageAdress = "./images/ennemy.jpg"
		self.image = None
		self.walkTick = 0
		self.walkTick_1 = 0
		self.path = []

		self.frames = 0


	def walk(self):
		self.frames +=1
		if not self.stun and not self.frames%8 : #walk activates each %x frames
			
			self.positionPrec = self.position[:]
			
			self.walkTick_1 += 1
			if self.walkTick_1 > len(self.pattern[self.walkTick])-1 :
				self.walkTick_1 = 0
				self.walkTick += 1
			if self.walkTick > len(self.pattern)-1 :
				self.walkTick = 0

			self.position = self.pattern[self.walkTick][self.walkTick_1][:]
	
	def updateVision(self):
		if self.positionPrec[0]-self.position[0] == 1  :
			self.direction = "left"
			self.vision = [
			[self.position[0]-1,self.position[1]],
			[self.position[0]-2,self.position[1]],
			[self.position[0]-3,self.position[1]],
			[self.position[0]-4,self.position[1]],
			[self.position[0]-5,self.position[1]],
			[self.position[0]-4,self.position[1]+1],
			[self.position[0]-5,self.position[1]+1],
			[self.position[0]-4,self.position[1]-1],
			[self.position[0]-5,self.position[1]-1]]

		elif self.positionPrec[0]-self.position[0] == -1 :
			self.direction = "right"
			self.vision = [
			[self.position[0]+1,self.position[1]],
			[self.position[0]+2,self.position[1]],
			[self.position[0]+3,self.position[1]],
			[self.position[0]+4,self.position[1]],
			[self.position[0]+5,self.position[1]],
			[self.position[0]+4,self.position[1]+1],
			[self.position[0]+5,self.position[1]+1],
			[self.position[0]+4,self.position[1]-1],
			[self.position[0]+5,self.position[1]-1]]

		elif self.positionPrec[1]-self.position[1] == 1 :
			self.direction = "up"
			self.vision = [
			[self.position[0],self.position[1]-1],
			[self.position[0],self.position[1]-2],
			[self.position[0],self.position[1]-3],
			[self.position[0],self.position[1]-4],
			[self.position[0],self.position[1]-5],
			[self.position[0]+1,self.position[1]-4],
			[self.position[0]+1,self.position[1]-5],
			[self.position[0]-1,self.position[1]-4],
			[self.position[0]-1,self.position[1]-5]]

		elif self.positionPrec[1]-self.position[1] == -1 :
			self.direction = "down"
			self.vision = [
			[self.position[0],self.position[1]+1],
			[self.position[0],self.position[1]+2],
			[self.position[0],self.position[1]+3],
			[self.position[0],self.position[1]+4],
			[self.position[0],self.position[1]+5],
			[self.position[0]+1,self.position[1]+4],
			[self.position[0]+1,self.position[1]+5],
			[self.position[0]-1,self.position[1]+4],
			[self.position[0]-1,self.position[1]+5]]


	def followPlayer(self):
		if not self.stun and not self.playerHandlerObject.hidden:
			a = randint(0,1)
			if (a == 0 and self.playerHandlerObject.position[0]!=self.position[0]) or (a == 1 and self.playerHandlerObject.position[1]!=self.position[1]) :
				if self.position[0] < self.playerHandlerObject.position[0]:
					self.position[0] +=1
				else:
					self.position[0] -=1
			elif (a == 0 and self.playerHandlerObject.position[1]!=self.position[1]) or (a == 1 and self.playerHandlerObject.position[0]!=self.position[0]):
				if self.position[1] < self.playerHandlerObject.position[1]:
					self.position[1] +=1
				else:
					self.position[1] -=1

			if self.playerHandlerObject.position[0] == self.position[0] and self.playerHandlerObject.position[1]==self.position[1]:
				print("jte bez")
		if not self.stun and self.playerHandlerObject.hidden:
			search()
			
	def search(self):
		if not self.stun and self.playerHandlerObject.hidden:
			pass

	def update(self):
		if self.playerHandlerObject.position in self.vision:
			self.followPlayer()
		else:
			self.walk()
		self.updateVision()

		"""
		for x in self.vision:
			self.graphicHandlerObject.displaySquare(x)"""
		self.graphicHandlerObject.displayActivatable(self)

	def pathfinder(self):
		tmp=[] # la liste tmp mémorise les données du tableau
		for i in range (self.levelHandlerObject.intersectionsCount):
			tmp.append([1000000,"X","N"])
		inter_select=0 # numéro de l'inter sélectionnée; 0 = inter de départ
		dist_interm=0 # distance pour arriver à l'inter sélectionnée; 0 au départ
		while inter_select != self.levelHandlerObject.intersectionsCount-1:
			minimum=1000000
			for n in range(1,self.levelHandlerObject.intersectionsCount):
				if tmp[n][2]=="N":
					dist=self.levelHandlerObject.intersectMatrix[inter_select][n]
					dist_totale=dist_interm+dist
					if dist != 0 and dist_totale < tmp[n][0]:
						tmp[n][0]=dist_totale
						tmp[n][1]=inter_select
					if tmp[n][0]<minimum:
						minimum=tmp[n][0]
						pinter_select=n
			inter_select=pinter_select # pinter_select = numéro de la prochaine inter sélectionnée
			tmp[inter_select][2]="O"
			dist_interm=tmp[inter_select][0]
		self.path=[] # reconstitution du plus court path, en partant de l'inter d'arrivée
		inter=self.intersectionsCount-1
		self.path.append(inter)
		while inter != 0:
			inter=tmp[inter][1]
			self.path.append(inter)
		self.path = self.path[::-1]
