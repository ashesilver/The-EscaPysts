#!/bin/usr/python3
# -*- coding:utf-8 -*-

var = {
	'lvl0':{"gate":{					#### gates are doors to go from teem to another in same level
				'image':'images/gate.jpg', 		   #### image Adresse 
				'position':[{},{},{}],
				#'size':["L","H"],
				'destination':[{},{},{}]  	  #### which room to go 
				},
			"flowerPot":{
			  	'image':'images/flowerPot.jpg',
			  	'position':[{},{},{}],
			  	#'size':['L','H'],
			  	'destination':[{},{},{}]
				},
			"path":{
				'image':'images/ground.jpg',
				'position' : [{},{},{}],
				#'size' : ['l','h'],
				'destination' : [{},{},{}]
				},
			"wall":{
				'image':'images/wall.jpg',
				'position' : [{},{},{}],
				#'size' : ['l','h'],
				'destination' : [{},{},{}]
				}
			},
	'lvl1':[{},{},{}],
	'lvl2':[{}]
}
