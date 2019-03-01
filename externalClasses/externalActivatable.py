#!/bin/usr/python3
# -*- coding:utf-8 -*-

class Activatable():
	"""Activatable  : classe des objets du niveau"""
	def __init__(self, name, obj, position, destination):
		self.type = name
		self.imageAdress = obj['image']
		self.size = obj['size']
		self.position = [position['x'],position['y']]
		self.destination = destination
		self.hideable = obj['hideable']

		#print(self.type)

	def update(self, graphicHandlerObject):
		graphicHandlerObject.displayActivatable(self)
