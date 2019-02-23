#!/bin/usr/python3
# -*- coding:utf-8 -*-

class Activatable():
	"""Activatable  : classe des objets du niveau"""
	def __init__(self, obj, position, destination):
		self.imageAdress = obj['image']
		self.size = obj['size']
		self.position = position
		self.destination = destination