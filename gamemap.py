import numpy as np
import random
import os 
import main

class MapMechanics():
    def __init__(self,xPos,yPos,xSize,ySize,worldMap,xShop,yShop):
        self.xPos = xPos
        self.yPos = yPos
        self.xSize = xSize
        self.ySize = ySize
        self.xShop = xShop
        self.yShop = yShop
        self.worldMap = worldMap
 
    def mapGenerate(self):
        self.worldMap = np.chararray((self.ySize,self.xSize), unicode = True)
        self.worldMap[:] = "`"


    def mapFunction(self):        
        self.mapGenerate()                 
        self.worldMap[self.yPos][self.xPos] = "x" #position of player
        try:
            self.worldMap[self.yShop][self.xShop] = "+" #position of shop
            print(self.worldMap)
        except IndexError:
            self.shopGenerate()
            self.mapFunction()

    def movePlayer(self):
        try:
            posChange = int(input("Move:\n1. East,\n2. West,\n3. North,\n4. South?\nInput: "))
            if posChange == 1:
                self.positionCheck(self.xPos, self.xPos + 1,"x")
            elif posChange == 2:
                self.positionCheck(self.xPos, self.xPos - 1,"x")
            elif posChange == 3:
                self.positionCheck(self.yPos, self.yPos - 1,"y")
            elif posChange == 4:
                self.positionCheck(self.yPos, self.yPos + 1,"y")
            else:
                print("What are you stupid??? I asked for 1-4.")
                self.movePlayer()
        except ValueError:
            print("Dude, honestly, you need help. Like what the actual fuck... I ask for a number so I can move you, and you have the fucking guts to come here and start with some shit that causes value errors.")
            print("The gumption...")
            self.movePlayer()    

    def positionCheck(self,initalPos,finalPos,direct):
        if (initalPos == self.xSize-1) and (finalPos-initalPos == 1) and (direct == "x"): #East
            self.xPos = 0
        elif (initalPos != self.xSize-1) and (finalPos-initalPos == 1) and (direct == "x"):
            self.xPos += 1

        if (initalPos == 0) and (finalPos-initalPos == -1) and (direct == "x"): #West
            self.xPos = self.xSize-1
        elif (initalPos != 0) and (finalPos-initalPos == -1) and (direct == "x"):
            self.xPos -= 1

        if (initalPos == 0) and (finalPos-initalPos == -1) and (direct == "y"): #North
            self.yPos = self.ySize-1
        elif (initalPos != 0) and (finalPos-initalPos == -1) and (direct == "y"):
            self.yPos -= 1

        if (initalPos == self.ySize-1) and (finalPos-initalPos == 1) and (direct == "y"): #South
            self.yPos = 0
        elif (initalPos != self.ySize-1) and (finalPos-initalPos == 1) and (direct == "y"):
            self.yPos += 1

        else:
            pass

    def shopGenerate(self):
        self.xShop = random.randint(0,self.xSize-1)
        self.yShop = random.randint(0,self.ySize-1)

    def shopRules(self):
        if (self.xPos == self.xShop) and (self.yPos == self.yShop):
            print("#########################\nYou have entered the shop\n#########################")
            #run something from shop.py

    def hostileEncounter(self):
        encounterChance = random.random()*100
        if encounterChance > 85:
            main.fight()


def mapLoop():
    a = MapMechanics(1,1,15,15,"","","")
    a.mapGenerate()
    a.mapFunction()
    for i in range(100):
        a.shopRules()
        a.movePlayer()
        a.hostileEncounter()
        os.system("cls")
        a.mapFunction()

mapLoop()

    
