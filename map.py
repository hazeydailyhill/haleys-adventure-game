import numpy as np
import random

class PlayerPos():
    def __init__(self,xPos,yPos,xSize,ySize):
        self.xSize = xSize
        self.ySize = ySize
        self.xPos = xPos
        self.yPos = yPos
 

    def worldMap(self):
        arrayMap = np.chararray((self.ySize,self.xSize), unicode = True)
        arrayMap[:] = "`"
        arrayMap[self.yPos][self.xPos] = "x" #position 
        x,y = self.shop() #This is to prove a point 
        arrayMap[x][y] = "0"#This is to prove a point 
        print(arrayMap)
        

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
        if (initalPos == self.xSize-1) and (finalPos-initalPos == 1) and (direct == "x"):
            self.xPos = 0
        elif (initalPos != self.xSize-1) and (finalPos-initalPos == 1) and (direct == "x"):
            self.xPos += 1

        if (initalPos == 0) and (finalPos-initalPos == -1) and (direct == "x"):
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
            
    def shop(self):
        randX = random.randint(0,self.xSize-1)
        randY = random.randint(0,self.ySize-1)
        #define shop interactables here
        return randX, randY

a = PlayerPos(1,1,10,10)
a.worldMap()



    
