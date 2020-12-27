import random
import math

class Enemy: #Create player functions: punch, kick, be bad at acting(i want this to be his most deadly weapon in a fight. Causes -30 damage), damage robert/health -= player1.punch
    def __init__(self, name, socialSecurityNumber, health, opponent):
        self.name = name 
        self.socialSecurityNumber = socialSecurityNumber
        self.health = health
        self.opponent = opponent

    def punch(self):
        if random.randint(0,10) %7 == 0:
            damage = 0
            print(self.name, "swings and misses")
        else:
            damage = random.randint(7,13)
            print(self.opponent,"has been punched for", damage, "damage.")
        return damage

    def kick(self):
        damage = random.randint(6,11)
        if random.randint(0,10) %5 == 0:
            damage -= 2
            print("His chicken legs provide a weak kick.")
        print(self.opponent, "has been kicked for", damage, "damage.")
        return damage 

    def actBadly(self):
        x = random.randint(0,800)
        damage = (8.1*(math.log(x+7.5,10))+1)//1
        print("Robert has begun doing improv, which deals a whopping", damage, "damage to",self.opponent+"'s psyche")
        return damage
    
    def damage(self):
        print(self.opponent, "has reduced Robert Pattinson's health to", self.health)
        return self.health

    def healthCheck(self):
        if self.health > 0:
            print(self.name+"'s health now:", self.health)
        else:
            print(self.name+" has been slain, thank God, his movies were crimes against humanity")
    
    def robertAttack(self):
        choice = random.randint(1,3)
        if choice == 1:
            return self.punch()
        elif choice == 2:
            return self.kick()
        else:
            return self.actBadly()

