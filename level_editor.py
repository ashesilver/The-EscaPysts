#!/bin/usr/python3
# -*- coding:utf-8 -*-

from externalClasses.externalGraphics import *

gr = Graphics()

clock = pygame.time.Clock()

quit = False

grid = [ [y for y in range (0,60)] for x in range (0,60) ]

common = []

Wsave = {"gate":{					#### gates are doors to go from teem to another in same level
				'image':'images/gate.jpg', 		   #### image Adresse 
				'position':[],
				'size':["L","H"],
				'destination':[],         #### which room to go
				'hideable':False 	   
				},
			"flowerPot":{
			  	'image':'images/flowerPot.jpg',
			  	'position' :[],
			  	'size':[1,1],
			  	'destination':[],
			  	'hideable':True
				},
			"noName":{
				'image':'images/ground.jpg',
				'position' : [],
				'size' : ['l','h'],
				'destination' : [],
				'hideable':False
				},
			"wall":{
				'image':'images/wall.png',
				'position' : [],
				'size' : [1,1],
				'destination' : [],
				'hideable':False
				}
			}
c1,c2,c3,c4,c5,c6 = 0,0,0,0,0,0

mode = "walls"
print("new mode : walls")

def onGridMousePos(x):
	return [int(x[0]/800*60),int(x[1]/800*60)]

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

		if "L" in keys :
			print("new mode : ennemies")
			mode = "ennemies"
		elif "R" in keys :
			print("new mode : walls")
			mode = "walls"
		if 'esc' in keys and mode == "ennemies":
			common = [[]]
			print("new ennemy")
		elif "U" in keys and mode == 'ennemies':
			common.append([])
			print("new row / column")
			c1 += 1

		if mode == "walls" :
			if gr.leftClick and not mousePos in Wsave["wall"]["position"]:
				Wsave["wall"]["position"].append(mousePos)
			elif gr.rightClick and mousePos in Wsave["wall"]["position"]:
				Wsave["wall"]["position"].remove(mousePos)
			for x in Wsave["wall"]["position"] :
				gr.displaySquare(x)
			if "enter" in keys or "ENTER" in keys :
				print(mode+ " " + str(Wsave))

		gr.generalDisplayUpdate()


#ajout gauche, supr droite
