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
		self.walkTick,self.walkTick_1,self.walkTick_2,self.walkTick_3,self.walkTick_4 = 0,0,0,0,0
		self.path = []
		self.lost = 0

		self.frames = 0
		self.lostFrames = 0
		self.triggered,self.searching = False,False

		self.backPath =[]
		self.overwriteVisionMethod = False
		self.previousBP = []


	def walk(self):
		if not self.stun and not self.frames%8 : #walk activates each %x frames
			
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
		if not self.stun and not self.frames%10:

			self.walkTick_2 += 1
			if self.walkTick_2 > len(self.path[self.walkTick_3])-1 :
				self.walkTick_2 = 0
				self.walkTick_3 += 1
			if self.walkTick_3 > len(self.path)-1 :
				self.walkTick_3 = 0

			self.position = self.path[self.walkTick_3][self.walkTick_2][:]
			self.previousBP.append(self.position)
		if self.position == self.lastSeenPosition:
			self.searching = True

	def cancelVision(self):
		for x in self.vision:
			if x in self.playerHandlerObject.walkLock:
				if self.direction == "left":
					for i in range(0,len(self.vision)):
						try :
							if (self.vision[i][1] == x[1] or (self.vision[i][1] == x[1]+1 and not self.vision[i] in self.playerHandlerObject.walkLock) or (self.vision[i][1] == x[1]-1 and not self.vision[i] in self.playerHandlerObject.walkLock)) and self.vision[i][0] <= x[0]:
								self.vision[i] = []
						except :
							pass
				elif self.direction == "right":
					for i in range(0,len(self.vision)):
						try :
							if (self.vision[i][1] == x[1] or (self.vision[i][1] == x[1]+1 and not self.vision[i] in self.playerHandlerObject.walkLock) or (self.vision[i][1] == x[1]-1 and not self.vision[i] in self.playerHandlerObject.walkLock)) and self.vision[i][0] >= x[0]:
								self.vision[i] = []
						except :
							pass
				elif self.direction == "up":
					for i in range(0,len(self.vision)):
						try :
							if (self.vision[i][0] == x[0] or (self.vision[i][0] == x[0]+1 and not self.vision[i] in self.playerHandlerObject.walkLock) or (self.vision[i][0] == x[0]-1 and not self.vision[i] in self.playerHandlerObject.walkLock)) and self.vision[i][1] <= x[1]:
								self.vision[i] = []
						except :
							pass
				elif self.direction == "down":
					for i in range(0,len(self.vision)):
						try :
							if (self.vision[i][0] == x[0] or (self.vision[i][0] == x[0]+1 and not self.vision[i] in self.playerHandlerObject.walkLock) or (self.vision[i][0] == x[0]-1 and not self.vision[i] in self.playerHandlerObject.walkLock)) and self.vision[i][1] >= x[1]:
								self.vision[i] = []
						except :
							pass
		self.vision = [x for x in self.vision if x != []]

	def search(self):
		if not self.stun and not self.frames%30:
			self.position = self.positionPrec[:]
			self.direction = choice(['up','down','left','right'])
			if self.direction == "left" :
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

			elif self.direction == "right":
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

			elif self.direction == "up" :
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

			elif self.direction == "down" :
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

			#self.backPath.append(self.position)

	def update(self,fps):
		self.positionPrec = self.position[:]
		if self.playerHandlerObject.position in self.vision:
			self.lastSeenPosition = self.playerHandlerObject.position[:]
			self.triggered = True
			self.searching = False
			self.lostFrames,self.walkTick_2,self.walkTick_3 = 0,0,0
			if self.direction == "up":
				self.path = [[[self.position[0],-y] for y in range(-self.position[1],-self.lastSeenPosition[1])],[[self.lastSeenPosition[0],self.lastSeenPosition[1]]]]
			elif self.direction == "right":
				self.path = [[[x,self.position[1]] for x in range(self.position[0],self.lastSeenPosition[0])],[[self.lastSeenPosition[0],self.lastSeenPosition[1]]]]
			elif self.direction == "down":
				self.path = [[[self.position[0],y] for y in range(self.position[1],self.lastSeenPosition[1])],[[self.lastSeenPosition[0],self.lastSeenPosition[1]]]]
			else :
				self.path = [[[-x,self.position[1]] for x in range(-self.position[0],-self.lastSeenPosition[0])],[[self.lastSeenPosition[0],self.lastSeenPosition[1]]]]
		if self.lostFrames > fps*2 :
			self.triggered = False
			self.walkTick_2,self.walkTick_3 = 0,0
			self.lostFrames = 0
			self.searching = False
			self.lost +=1
			self.overwriteVisionMethod = False
			self.backPath = self.previousBP[::-1]
			tmp = [self.backPath[0]]
			for i in range(1,len(self.backPath)):
				if not self.backPath[i-1] == self.backPath[i] :
					tmp.append(self.backPath[i])
			self.backPath = tmp[:]

		self.frames = 0 if self.frames > 1000000 else self.frames + 1

		if not self.triggered and self.lost > 0:
			if not self.frames%8 :
				self.position = self.backPath[0][:]
				if len(self.backPath)-1 == 0:
					self.lost = 0
				else :
					self.backPath.remove(self.backPath[0])
		elif not self.triggered :
			self.walk()
			self.backPath,self.previousBP = [],[]
			self.walkTick_4 = 0
		elif self.playerHandlerObject.hidden or self.searching:
			self.search()
			self.lostFrames += 1
			self.overwriteVisionMethod = True		
		else :
			self.followPlayer()
			self.overwriteVisionMethod = False
		
		if not self.overwriteVisionMethod :
			self.updateVision()
		self.cancelVision()

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
