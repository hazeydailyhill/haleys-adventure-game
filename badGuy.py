import random

class Enemy: #Create player functions: punch, kick, be bad at acting(i want this to be his most deadly weapon in a fight. Causes -30 damage), damage robert/health -= player1.punch
    def __init__(self, name, socialSecurityNumber, health):
        self.name = name 
        self.socialSecurityNumber = socialSecurityNumber
        self.health = health

    def punch(self):
        print("player 1 has been punched for 15 damage")
        return 15

    def kick(self):
        print("player 1 has been kicked for 10 damage")
        return 10

    def actBadly(self):
        print("Robert has begun doing improv, which deals a whopping 30 damage to player 1's psyche")
        return 30
    
    def damage(self):
        print("player 1 has reduced Robert Pattinson's health to", self.health)
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

