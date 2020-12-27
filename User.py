import random 
import art

class Player: #Create player functions: startFight, punch, kick, curbstomp, steal identity (get his social security number and attain his wealth)
    def __init__(self, name, age, height, socialSecurityNumber, health, enemy):
        self.name = name 
        self.age = age
        self.height = height
        self.socialSecurityNumber = socialSecurityNumber
        self.health = health
        self.enemy = enemy
    
    def stealIdentity(self, socialSecurityNumber):
         print("Congratulations, you have weakened robert by 30% and you now control all of his wealth")
         return 30

    def damage(self):
        print("the enemy has reduced your health to", self.health)
        return self.health

    def punch(self):
        bleed = False
        if random.randint(0,100) <= 5:
            print("your attack failed")
            damage = 0
        else:
            damage = random.randint(7, 15)
            if damage >= 10:
                bleed = True
                print("bleed")
            print("You have punched", self.enemy, "for",damage, "damage")
        return damage, bleed 

    def kick(self):
        damage = random.randint(6, 12)
        if random.randint(0,10) %7 == 0:
            damage *= 2
            art.criticalHit()
        print("You have kicked", self.enemy, "for", damage, "damage")
        return damage
    
    def curbstomp(self):
        if random.randint(0,10) %2 == 0:
            damage = 0 
            print("you missed. please practice your curbstomping")
        else:
            damage = random.randint(15,27)
            print("You have successfully curb stomped for", damage, "damage")
        return damage
    
    def heal(self):
        self.health += 14
        print("You have healed to", self.health, "health. nice.")
    
    def attackChoice(self):
        userIn = int(input("choose your attack! (enter a number)\n 1. Punch \n 2. Kick \n 3. Curb Stomp\n 4. Heal(coward) \n Input: "))
        if userIn == 1: #punch
            return self.punch()
        elif userIn == 2: #kick 
            return self.kick(), False
        elif userIn == 3: #curbstomp
            return self.curbstomp(), False
        elif userIn == 4: #health
            self.heal()
            return 0, False
        else:
            print("input not recognized, turn skipped, eat farts")
            return 0, False
    
    
def newPlayer():
    name = str(input("what is your name? "))
    age = str(input("how old are you? " ))
    height = str(input("how tall are you? "))
    socialSecurityNumber = str(input("what is your social security number? "))
    return name, age, height, socialSecurityNumber 