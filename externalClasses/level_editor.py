#!/bin/usr/python3
# -*- coding:utf-8 -*-

from externalGraphics import *

import os

gr = Graphics()

clock = pygame.time.Clock()

quit = False

grid = [ [y for y in range (0,60)] for x in range (0,60) ]

common = []

Wsave = {
	"gate":{
		'image':['images/gate.jpg','images/openGate.png'],
		'position':[],
		'size':[1,1],
		'destination':[],
		'hideable':False 	   
		},
	"flowerPot":{
	  	'image':['images/flowerPot.jpg'],
	  	'position' :	[],
	  	'size':[1,1],
	  	'destination':	[],
	  	'hideable':True
		},
	"key":{
		'image':['images/key.jpg'],
		'position' : [],
		'size' : [1,1],
		'destination' : [],
		'hideable':False
		},
	"wall":{
		'image':['images/wall.png'],
		'position' : 	[],
		'size' : [1,1],
		'destination' : [],
		'hideable':False
		}
	}
common = [[]]

c1=0

keysRegister = []

allEnnemies = []

helper = "flèches :\n gauche -> passer en mode 'ennemis'\n droite -> passer en mode 'mur' (par défault)\n haut -> chager de direction pour les ennemis\n bas -> créer un nouvel ennemis (et enregistrer le précedent)\nEntrée (pav num et principal) :\n afficher la référence à copier-coller\néchap :\n affiche cette aide\nclics :\n gauche -> ajouter position\n droite -> enlever position\n\n"

mode = "walls"
print("new mode : walls")

def onGridMousePos(x):
	return [int(x[0]/800*60),int(x[1]/800*60)]

def keyLock(keys,keysRegister):
	for x in ["U","L","D","R","Enter","ENTER","esc","1","2","3","4"]:
		if ( not x in keys) and x in keysRegister :
			keysRegister.remove(x)
		elif x in keysRegister:
			keys.remove(x)
		elif x in keys and not x in keysRegister:
			keysRegister.append(x)
	return (keys,keysRegister)

gr.displayBackgroundUpdate("images/lvl0.png")

while not quit :
	clock.tick(120)
	keys = gr.getKeys()
	if type(keys)==bool :
		pygame.quit() 
		quit = True

	else :
		gr.displayBackgroundUpdate()

		gr.drawGrid()

		mousePos = onGridMousePos(gr.getMouse())[:]

		x = keyLock(keys,keysRegister)
		keys,keysRegister = x[0][:],x[1][:]

		if "esc" in keys :
			print(helper)

		if "L" in keys :
			print("new mode : ennemies")
			mode = "ennemies"
		elif "R" in keys :
			print("new mode : walls")
			mode = "walls"

		if mode == "walls" :

			if gr.leftClick and not mousePos in Wsave["wall"]["position"]:
				Wsave["wall"]["position"].append({'x' : mousePos[0],'y' : mousePos[1] })
				Wsave["wall"]["destination"].append({'x' : mousePos[0],'y' : mousePos[1] })
			elif gr.rightClick and mousePos in Wsave["wall"]["position"]:
				Wsave["wall"]["position"].remove({'x' : mousePos[0],'y' : mousePos[1] })
				Wsave["wall"]["destination"].remove({'x' : mousePos[0],'y' : mousePos[1] })
			
			for x in Wsave["wall"]["position"] :
				gr.displaySquare(x)
			
			if ("enter" in keys) or ("ENTER" in keys):
				if os.name == "posix" :
					os.system("clear")
				elif os.name == "nt" :
					os.system("cls")
				print(mode+ " " + str(Wsave))

		elif mode == "ennemies" :

			if 'D' in keys:
				allEnnemies.append(common)
				common = [[]]
				c1 = 0
				print("new ennemy pattern")
			
			elif "U" in keys:
				common.append([])
				print("new row / column")
				c1 += 1
			
			if ( "enter" in keys ) or ("ENTER" in keys) :
				if os.name == "posix" :
					os.system("clear")
				elif os.name == "nt" :
					os.system("cls")
				print(mode+ " " + str(allEnnemies))
			
			if gr.leftClick and not mousePos in common[c1]:
				common[c1].append(mousePos)
			elif gr.rightClick and mousePos in common[c1] :
				common[c1].remove(mousePos)

			for x in Wsave["wall"]["position"] :
				gr.displaySquare(x,1)
			for x in common:
				for y in x :
					if x != common[c1] :
						gr.displaySquare(y,2)
			for x in common[c1] :
				gr.displaySquare(x)
				
		gr.generalDisplayUpdate()


input("      press enter to kill this window")