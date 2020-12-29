import random
import os
import time
import gameMechanics
import art
import fight
import gamemap
from badGuy import *
from User import *

def gameLoop():
    a = gamemap.MapMechanics(1,1,15,15,"","","")
    a.mapGenerate()
    a.mapFunction()
    for i in range(100):
        a.shopRules()
        a.movePlayer()
        fight.hostileEncounter()
        os.system("cls")
        a.mapFunction()

#art.titleScreen()
gameLoop()
art.credits()