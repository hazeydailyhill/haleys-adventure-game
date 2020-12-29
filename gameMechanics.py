import random
import math
import art

def healthBar(health, bleed):
    healthCounter = health//5
    healthBar = "["
    for i in range(healthCounter): #length of amount of health
        healthBar += "="
    for i in range(20 - healthCounter): #length of amount of lost health
        healthBar += "-"
    healthBar += "]"
    if bleed == True:
        statement = "Bleeding"
    else:
        statement = "Not Bleeding"
    print(healthBar, "\n"+statement)

def healthCheck(name, health, bleed): #player
    if health > 0:
        print(name+"'s health now:", health)
    healthBar(health, bleed)

def damageCheck(victim, dmg, bleed, guard): #victim reps the health of the person getting punched
    if dmg > 0: 
        if (guard == True) and (random.randint(0,1) == 1):
            dmg = 0 
            print("DAMAGE BLOCKED!!!")
            guard = False
        elif guard == True:
            print("BLOCK MISSED!!!")
            guard = False
        victim -= dmg
    if bleed == True:
        victim -= 1
    return victim, guard

def damageProbability(maximumDamage, probabilityMultiplier, baseDamage):
    x = random.random()
    damage = int((maximumDamage*(x*math.exp(probabilityMultiplier*(x-1))+baseDamage))//1)
    return damage 

def punch(enemy, name):
    bleed = False
    if random.randint(0,100) <= 5:
        print(name+" swings and misses")
        damage = 0
    else:
        damage = random.randint(7, 15)
        if damage >= 10:
            bleed = True
            art.bleedHit()
        print(name, "punched", enemy, "for",damage, "damage")
    return damage, bleed 

def heal(health, name):
    health += 14
    print(name,"healed to", health, "health. nice.")
    return health, False

def bodySlam(enemy, name):
    if random.randint(0,100) > 70:
        damage = 0
        print(name, "failed to bodyslam", enemy, "for", damage, "damage. Bummer.")
    else: 
        damage = damageProbability(20, 3, .5)
        print(name, "bodyslammed", enemy, "for", damage, "damage. Alright.")
    return damage

