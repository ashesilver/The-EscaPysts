#!/bin/usr/python3
# -*- coding:utf-8 -*-

var = {
	'lvl0':{"gate":{					#### gates are doors to go from teem to another in same level
				'image':'images/gate.jpg', 		   #### image Adresse 
				'position':[],
				'size':["L","H"],
				'destination':[],         #### which room to go
				'hideable':False 	   
				},
			"flowerPot":{
			  	'image':'images/flowerPot.jpg',
			  	'position':[{'x':35,'y':10}],
			  	'size':[1,1],
			  	'destination':[{}],
			  	'hideable':True
				},
			"path":{
				'image':'images/ground.jpg',
				'position' : [],
				'size' : ['l','h'],
				'destination' : [],
				'hideable':False
				},
			"wall":{
				'image':'images/wall.png',
				'position' : [{'x':20,'y':30},{'x':45,'y':65},{'x':10,'y':45}],
				'size' : [1,1],
				'destination' : [],
				'hideable':False
				}
			},
	'lvl1':[{},{},{}],
	'lvl2':[{}]
}
