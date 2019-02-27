#!/bin/usr/python3
# -*- coding:utf-8 -*-

var = {
	'lvl0':{"gate":{					#### gates are doors to go from teem to another in same level
				'image':'./gate.jpg', 		   #### image Adresse 
				'position':[{},{},{}],
				#'size':["L","H"],
				'destination':[{},{},{}]  	  #### which room to go 
				},
			"hideout":{
			  	'image':'Image Adresse',
			  	'position':[{},{},{}],
			  	#'size':['L','H'],
			  	'destination':[{},{},{}]
				},
			"path":{
				'image':'adress',
				'position' : [{},{},{}],
				#'size' : ['l','h'],
				'destination' : [{},{},{}]
				},
			"wall":{
				'image':'adress',
				'position' : [{},{},{}],
				#'size' : ['l','h'],
				'destination' : [{},{},{}]
				}
			},
	'lvl1':[{},{},{}],
	'lvl2':[{}]
}
