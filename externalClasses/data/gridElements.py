#!/bin/usr/python3
# -*- coding:utf-8 -*-

var = {
	'lvl0':{"gate":{					#### gates are doors to go from teem to another in same level
				'image':['images/gate.jpg','images/openGate.png'], 		   #### image Adresse 
				'position':[{'x':42,'y':50}],
				'size':[1,1],
				'destination':[{'x':42,'y':50}],         #### which room to go
				'hideable':False 	   
				},
			"flowerPot":{
			  	'image':['images/flowerPot.jpg'],
			  		'position' :	[{'x':35,'y':10},
			  				{ 'x':36,'y':10},
			  				{ 'x':35,'y':11},
			  				{ 'x':36,'y':11}
			  	],
			  	'size':[1,1],
			  	'destination':	[{'x':35,'y':10},
			  			{ 'x':36,'y':10},
			  			{ 'x':35,'y':11},
			  			{ 'x':36,'y':11}
			  	],
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
				'position' : 	[{'x':20,'y':30},
								{'x':22,'y':30},
								{'x':24,'y':30},
								{'x':26,'y':30},
								{'x':28,'y':30},
								{'x':30,'y':30},
								{'x':32,'y':30},
								{'x':34,'y':30},
								{'x':36,'y':30},
								{'x':38,'y':30},
								{'x':40,'y':30},
								{'x':42,'y':30},
								{'x':44,'y':30},
								{'x':46,'y':65},
								{'x':10,'y':45}
								],
				'size' : [1,1],
				'destination' : [{'x':20,'y':30},
								{'x':22,'y':30},
								{'x':24,'y':30},
								{'x':26,'y':30},
								{'x':28,'y':30},
								{'x':30,'y':30},
								{'x':32,'y':30},
								{'x':34,'y':30},
								{'x':36,'y':30},
								{'x':38,'y':30},
								{'x':40,'y':30},
								{'x':42,'y':30},
								{'x':44,'y':30},
								{'x':46,'y':65},
								{'x':10,'y':45}
								],
				'hideable':False
				}
			},
	'lvl1':{}
	'lvl2':{}
}
