#!/bin/usr/python3
# -*- coding:utf-8 -*-

###### external files

from externalClasses.externalCore import *

#///////////////////////////////// execution

game = Core(100)
game.run()
print("\nsucessfully executed : The EscaPysts\nSee you soon !\n")
input("Press Enter to kill this window.")
del game
quit()