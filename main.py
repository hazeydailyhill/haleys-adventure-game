import random
from badGuy import *
from User import *


#IM RUNNING THINGS BELOW HERE!!!!!!!
#w,x,y,z = newPlayer() #w= name, x= age, y= height, z=SS#, ENTERED 100 FOR HEALTH, ENTERED ROBERT FOR ENEMY
#player1 = Player(w,x,y,z,100,Robert)
player1 = Player("Haley",19,0,1,100, "Robert Pattinson")
#print(player1.name)
#print(player1.health)



robert = Enemy("Robert Pattinson", 1234567, 100)
while robert.health > 0 and player1.health > 0:
    print("\n"+player1.name+"'s turn"+"\n")
    robert.health -= player1.attackChoice()
    robert.healthCheck()
    print("\n"+robert.name+"'s turn"+"\n")
    player1.health -= robert.robertAttack()
    player1.healthCheck()

