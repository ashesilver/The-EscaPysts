#!/bin/usr/python3
# -*- coding:utf-8 -*-

class Activatable():
	"""Activatable  : classe des objets du niveau"""
	def __init__(self, name, obj, position, destination):
		self.type = name
		self.imageAdresses = obj['image']
		self.size = obj['size']
		self.position = [position['x'],position['y']]
		self.destination = destination
		self.hideable = obj['hideable']
		self.image = None
		if self.type == "key" :
			self.picked = False
		elif self.type == "gate" :
			self.open = False
		self.needUpdate = True
		self.imageAdress = self.imageAdresses[0]
		#print(self.type)

	def update(self, graphicHandlerObject):
		if self.type == "wall":
			graphicHandlerObject.displayActivatable(self,True,False)
		if self.type == 'gate':
			if self.open and self.needUpdate:
				self.imageAdress = self.imageAdresses[1]
				self.image = None
				self.needUpdate = False
		if self.type == 'key':
			if self.picked :
				del self
			else :
				graphicHandlerObject.displayActivatable(self)
		else:
			graphicHandlerObject.displayActivatable(self)
		