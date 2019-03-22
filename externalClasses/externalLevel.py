#!/bin/usr/python3
# -*- coding:utf-8 -*-

import externalClasses.data.gridElements as gameplayElements
import externalClasses.data.EnnemiesPattern as ennemiesPat

from externalClasses.externalActivatable import *
from externalClasses.externalEnnemies import *

class Level():
	"""Level : gestionnaire du niveau en cours"""

	def __init__(self, arg, player=None):
		self.graphicHandlerObject = arg

		self.memoryPath()
		self.id = int(self.save)

		self.selector = {}
		self.locator = []

		tmp = gameplayElements.var["lvl"+str(self.id)]
		self.elements = [ [ Activatable(x,tmp[x],tmp[x]['position'][i],tmp[x]['destination'][i]) for i in range(0,len(tmp[x]['position'])) ] for x in tmp ] #stores in 1 attribute/self.gridElements/ all grid elements in gridElements.py (external file)
		
		self.grid = [ [y for y in range (0,60)] for x in range (0,60) ] #bigger grid (*2)

		tmp = ennemiesPat.var["lvl"+str(self.id)]
		self.ennemies= [ Ennemies(self.graphicHandlerObject,self,player,x) for x in tmp ]

		self.imageAdress = "./images/lvl"+str(self.id)+".png"
		self.graphicHandlerObject.displayBackgroundUpdate(self.imageAdress)

		self.elements = [x for x in self.elements if x != []]
		for x in self.elements :
			for y in x :
					#print("trying to display "+y.type+ " at : "+ str(y.position))
					y.update(self.graphicHandlerObject)				
					#print("sucessfully displayed "+y.type+ " at : "+ str(y.position))

		self.intersectMatrix = [[]]

	def update(self,fps):
		for x in self.elements :
			for y in x :
					#print("trying to display "+y.type+ " at : "+ str(y.position))
					y.update(self.graphicHandlerObject)				
					#print("sucessfully displayed "+y.type+ " at : "+ str(y.position))
		for x in self.ennemies :
			x.update(fps)

	def memoryPath(self):
		self.savefile = "externalClasses/data/save.txt"

		try :
			fichier = open(self.savefile,"r")
		except:
			fichier = open(self.savefile,"w")
			fichier.write("0")
			fichier.close()
			fichier = open(self.savefile,"r")
		finally:
			self.save = int(fichier.read())
			fichier.close()

	def matrix(self):
		listInters = []
		for a in self.playerHandlerObject.walkLock :
			x = [a[0]+1,a[1]]
			if not x in self.playerHandlerObject.walkLock :
				listInters.append(x)
			x = [a[0]-1,a[1]]
			if not x in self.playerHandlerObject.walkLock :
				listInters.append(x)
			x = [a[0],a[1]+1]
			if not x in self.playerHandlerObject.walkLock :
				listInters.append(x)
			x = [a[0],a[1]-1]
			if not x in self.playerHandlerObject.walkLock :
				listInters.append(x)

		tmp =[]
		for x in listInters :
			if not x in tmp :
				tmp.append(x)


		self.intersectMatrix = [ [0 for x in range(len(tmp))] for y in range(len(tmp))]

		for x in tmp :
			for y in tmp:
				if abs(x[0]-y[0])<2 or abs(x[1]-y[1])<2 :
					self.intersectMatrix[tmp.index(x)][tmp.index(y)] = 1
					self.intersectMatrix[tmp.index(y)][tmp.index(x)] = 1
		self.intersectionsCount = len(tmp)

		#print(self.intersectMatrix)

	def save(self):
		self.id += 1
		fichier = open(self.savefile,"w")
		fichier.write(str(self.id))
		fichier.close()

	def test(self):
		print(self.grid)

