#!/bin/usr/python3
# -*- coding:utf-8 -*-

var = {
	'lvl0':[{ "gate":[{					#### gates are doors to go from teem to another in same level
				'image':'./gate.jpg', 		   #### image Adresse 
				'positions':[{},{},{}],
				'size':[{"L"},{"H"}],
				'destination':[{},{},{}]  	  #### which room to go 
				}]
			},{
			  "hideout":[{
			  	'image':'Image Adresse',
			  	'positions':[{},{},{}],
			  	'size':[{'L'},{'H'}]
				}]
			}],
	'lvl1':[{},{},{}],
	'lvl2':[{}]
}
