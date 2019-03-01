#!/bin/usr/python3
# -*- coding:utf-8 -*-

import externalClasses.data.gridElements as gameplayElements

from externalClasses.externalActivatable import *
from externalClasses.externalEnnemies import *

class Level():
	"""Level : gestionnaire du niveau en cours"""

	def __init__(self, arg=None):
		self.memoryPath()
		self.id = int(self.save)

		self.selector = {}
		self.locator = []

		tmp = gameplayElements.var["lvl"+str(self.id)]
		self.elements = [ [ Activatable(x,tmp[x],tmp[x]['position'][i],tmp[x]['destination'][i]) for i in range(0,len(tmp[x]['position'])) ] for x in tmp ] #stores in 1 attribute/self.gridElements/ all grid elements in gridElements.py (external file)
		self.graphicHandlerObject = arg
		self.grid = [ [y for y in range (0,40*2)] for x in range (0,30*2) ] #bigger grid (*2)

		self.graphicHandlerObject.displayBackgroundUpdate("./images/lvl"+str(self.id)+".jpg")

		self.elements = [x for x in self.elements if x != []]
		print(self.elements)
		for x in self.elements :
			for y in x :
					#print("trying to display "+y.type+ " at : "+ str(y.position))
					y.update(self.graphicHandlerObject)				
					#print("sucessfully displayed "+y.type+ " at : "+ str(y.position))

	def update(self):
		for x in self.elements :
			for y in x :
					#print("trying to display "+y.type+ " at : "+ str(y.position))
					y.update(self.graphicHandlerObject)				
					#print("sucessfully displayed "+y.type+ " at : "+ str(y.position))

		self.graphicHandlerObject.generalDisplayUpdate()

	def memoryPath(self):
		self.savefile = "save.txt"

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

	def save(self):
		self.id += 1
		fichier = open(self.savefile,"w")
		fichier.write(str(self.id))
		fichier.close()

	def test(self):
		print(self.grid)

