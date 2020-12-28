import random 
import art
import gameMechanics
import os

class Player: #Create player functions: startFight, punch, kick, curbstomp, steal identity (get his social security number and attain his wealth)
    def __init__(self, name, age, height, socialSecurityNumber, health, enemy, bleed):
        self.name = name 
        self.age = age
        self.height = height
        self.socialSecurityNumber = socialSecurityNumber
        self.health = health
        self.enemy = enemy
        self.bleed = bleed
    
    def stealIdentity(self, socialSecurityNumber):
         print("Congratulations, you have weakened robert by 30% and you now control all of his wealth")
         return 30

    def damage(self):
        print("the enemy has reduced your health to", self.health)
        return self.health

    def kick(self):
        damage = random.randint(6, 12)
        if random.randint(0,10) %7 == 0:
            damage *= 2
            art.criticalHit()
        print("You have kicked", self.enemy, "for", damage, "damage")
        return damage
    
    def curbstomp(self):
        if random.randint(0,100) >= 75:
            damage = 0 
            print("you missed. please practice your curbstomping")
        else:
            damage = gameMechanics.damageProbability(30, 5, 5)
            print("You have successfully curb stomped for", damage, "damage")
        return damage
    
    def attackChoice(self):
        os.system("cls")
        try:
            userIn = int(input("choose your attack! (enter a number)\n 1. Punch \n 2. Kick \n 3. Curb Stomp \n Input: "))
            if userIn == 1: #punch
                return gameMechanics.punch(self.enemy, self.name)
            elif userIn == 2: #kick 
                return self.kick(), False
            elif userIn == 3: #curbstomp
                return self.curbstomp(), False
            else:
                print("input not recognized, turn skipped, eat farts")
                return 0, False
        except ValueError:
            print("that's not even a number, turn skipped, eat farts")
            return 0, False
    
    def menu(self):
        try:
            userIn = int(input("Choose your move! \n1. Attack \n2. Defend \n3. Action \n Input: "))
            if userIn ==1: #attack
                return self.attackChoice()
            elif userIn ==2: #Defend
                print("slow your roll speedracer, we don't know how to set that up yet")
                return 0, False
            elif userIn == 3: #Action
                return self.action()
            else:
                print("read, please.")
                return 0, False
        except ValueError:
            print("that's not even a number, turn skipped, eat farts")
            return 0, False
        

    def action(self):
        os.system("cls")
        try:
            userIn = int(input("Choose your move! \n1. Heal \n2. Exit Game (coward)\n Input: "))
            if userIn ==1: #heal
                self.health, self.bleed = gameMechanics.heal(self.health, self.name)
                return 0, False
            elif userIn ==2: #Flee
                print("You cant run or hide yet")
                exit()
            else:
                print("read, please.")
                return 0, False
        except ValueError:
            print("that's not even a number, turn skipped, eat farts")
            return 0, False
    
def newPlayer():
    name = str(input("what is your name? "))
    age = str(input("how old are you? " ))
    height = str(input("how tall are you? "))
    socialSecurityNumber = str(input("what is your social security number? "))
    return name, age, height, socialSecurityNumber 