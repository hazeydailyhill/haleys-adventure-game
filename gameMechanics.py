def healthBar(health):
    healthCounter = health//5
    healthBar = "["
    for i in range(healthCounter): #length of amount of health
        healthBar += "="
    for i in range(20 - healthCounter): #length of amount of lost health
        healthBar += "-"
    healthBar += "]"
    print(healthBar)

def healthCheck(name,health): #player
    if health > 0:
        print(name+"'s health now:", health)
    healthBar(health)

def damageCheck(victim, dmg, bleed): #victim reps the health of the person getting punched
    victim -= dmg
    if bleed:
        victim -= 1
    return(victim)