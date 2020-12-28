import random
import math
import gameMechanics

class Enemy: #Create player functions: punch, kick, be bad at acting(i want this to be his most deadly weapon in a fight. Causes -30 damage), damage robert/health -= player1.punch
    def __init__(self, name, socialSecurityNumber, health, opponent, bleed, guard):
        self.name = name 
        self.socialSecurityNumber = socialSecurityNumber
        self.health = health
        self.opponent = opponent
        self.bleed = bleed #bleed damage stat is a boolean (either bleeding or not TF)
        self.guard = guard

    def kick(self):
        damage = gameMechanics.damageProbability(12, 3, .7)
        if random.randint(0,10) %5 == 0:
            damage -= 2
            print("His chicken legs provide a weak kick.")
        print(self.opponent, "has been kicked for", damage, "damage.")
        return damage 

    def actBadly(self):
        damage = gameMechanics.damageProbability(25, 5, .6)
        print("Robert has begun doing improv, which deals a whopping", damage, "damage to",self.opponent+"'s psyche")
        return damage
    
    def damage(self):
        print(self.opponent, "has reduced Robert Pattinson's health to", self.health)
        return self.health

    def heal(self):
        self.health += 10
        print(self.name, "has healed to", self.health, "health. nice.")
        self.bleed = False


    def robertAttack(self):
        if self.health > 50:
            if self.bleed:
                choice = random.randint(1,4)
            else:
                choice = random.randint(1,3)
            if choice == 1:
                return gameMechanics.punch(self.opponent, self.name)
            elif choice == 2:
                return self.kick(), False
            elif choice == 3:
                return self.actBadly(), False
            else:
                self.health, self.bleed = gameMechanics.heal(self.health, self.name)
                return 0, False
        else:
            if self.bleed == False:
                choice = random.randint(0,100)
                if (choice >= 40) and (choice < 60):
                    return gameMechanics.punch(self.opponent, self.name)
                elif (choice >= 60) and (choice < 80):
                    return self.kick(), False
                elif (choice >= 80) and (choice < 100):
                    return self.actBadly(), False
                elif (choice >= 20) and (choice < 40):
                    self.guard = True
                    print(self.name, "has his guard up")
                    return 0, False
                else:
                    self.health, self.bleed = gameMechanics.heal(self.health, self.name)
                    return 0, False
            else:
                choice = random.randint(0,100)
                if (choice >= 30) and (choice < 40):
                    return gameMechanics.punch(self.opponent, self.name)
                elif (choice >= 40) and (choice < 50):
                    return self.kick(), False
                elif (choice >= 50) and (choice < 70):
                    return self.actBadly(), False
                elif (choice >= 20) and (choice < 30):
                    self.guard = True
                    print(self.name, "has his guard up")
                    return 0, False
                else:
                    self.health, self.bleed = gameMechanics.heal(self.health, self.name)
                    return 0, False
        
