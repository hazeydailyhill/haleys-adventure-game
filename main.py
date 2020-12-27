import random
import os
import time
import credits1
import gameMechanics
from badGuy import *
from User import *


#IM RUNNING THINGS BELOW HERE!!!!!!!
#w,x,y,z = newPlayer() #w= name, x= age, y= height, z=SS#, ENTERED 100 FOR HEALTH, ENTERED ROBERT FOR ENEMY
#player1 = Player(w,x,y,z,100,Robert)
player1 = Player("Haley",19,0,1,100, "Robert Pattinson")
#print(player1.name)
#print(player1.health)



robert = Enemy("Robert Pattinson", 1234567, 100, player1.name, False)
os.system("cls")
while robert.health > 0 and player1.health > 0:
    print("\n"+player1.name+"'s turn"+"\n")
    initialBleed = robert.bleed
    directDamage, robert.bleed = player1.attackChoice()
    if initialBleed != robert.bleed:
        robert.bleed = True
    robert.health = gameMechanics.damageCheck(robert.health, directDamage, robert.bleed)
    gameMechanics.healthCheck(robert.name, robert.health)
    time.sleep(1)
    if robert.health > 0:
        print("\n"+robert.name+"'s turn"+"\n")
        player1.health = gameMechanics.damageCheck(player1.health, robert.robertAttack(), False)
        gameMechanics.healthCheck(player1.name, player1.health)
    else:
        art.victoryAnimation()
        print(robert.name+" has been slain, thank God, his movies were crimes against humanity")
    if player1.health <= 0:
        art.deathAnimation()
        print(player1.name+" has died. The world deserved more.")
    #robert.health = 0 
    cont = input("\nhit enter to continue...\n")
    os.system("cls")
credits1.credits()