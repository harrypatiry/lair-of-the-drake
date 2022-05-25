import os, random, sys

run = True
menu = True
play = False
rules = False
key = False
fight = True
standing = True
trade_lief = False
trade_galren = False
trade_stolig = False
speak = False
boss = False

HP = 50 #health
HPMAX = 50
ATK = 5 #attack
PTN = 1 #potion
ELX = 0 #elixer
GLD = 100 #gold
HGR = 50 #hunger
HGRMAX = 50
FOOD = 2
x = 0
y = 0

        #  x = 0       x = 1       x = 2       x = 3       x = 4       x = 5         x = 6       x = 7
# map = [["plains",   "plains",   "plains",   "plains",    "plains",    "forest", "mountain",       "cave"],    # y = 0
#        ["plains",   "forest",   "forest",   "forest",    "galren",    "forest",    "hills",   "mountain"],    # y = 1
#        ["plains",   "forest",   "fields",   "bridge",    "plains",     "hills",   "forest",      "hills"],    # y = 2
#        ["plains",   "plains",     "lief",     "town", "displacer",    "stolig",    "hills",   "mountain"],    # y = 3
#        ["plains",   "plains",   "fields",   "fields",    "plains",     "hills", "mountain",   "mountain"],    # y = 4
#        ["plains",   "plains",   "fields",   "fields",    "plains",     "hills", "mountain",   "mountain"],    # y = 5
#        ["plains",   "plains",   "fields",   "fields",    "plains",     "hills", "mountain",   "mountain"],    # y = 6
#        ["plains",   "plains",   "fields",   "fields",    "plains",     "hills", "mountain",   "mountain"]]    # y = 7
#        0    1    2    3    4    5    6    7    8    9    10   11   12  13   14   15   16   17
map = [[  1,   1, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], # 0
       ['P',   1,   1, 'X', 'X',   1,   1,   1, 'T', 'T',   1, 'X', 'X', 'X', 'X', 'X',   1, 'B'], # 1
       ['P',   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 'X', 'X', 'X', 'X',   1, 'X'], # 2
       ['P', 'X',   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 'X', 'C',   1,   1, 'X'], # 3
       ['P', 'X',   1,   1,   1, 'X',   1,   1,   1,   1,   1,   1,   1,   1,   1, 'X', 'X', 'X'], # 4
       ['P', 'M',   1,   1,   1,   1,   1, 'L',   1, 'X', 'D',   1,   1,   1,   1,   1, 'X', 'X'], # 5
       ['P', 'M',   1,   1,   1,   1,   1,   1, 'X', 'H', 'X',   1,   1,   1,   1,   1,   1, 'X'], # 6
       ['P', 'H',   1,   1,   1,   1,   1,   1,   1, 'X', 'X',   1,   1,   1,   1,   1,   1, 'X'], # 7
       ['P', 'X',   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 'T', 'T',   1,   1,   1], # 8
       ['P', 'X',   1,   1, 'X',   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 'X'], # 9
       ['P', 'X',   1, 'X', 'M', 'X',   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 'X'], # 10
       ['P', 'X', 'X', 'X', 'M', 'X',   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 'X'], # 11
       ['P', 'X', 'X',   1, 'G', 'X',   1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 'X', 'X'], # 12
       ['P', 'X',   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 'H', 'X'], # 13
       ['P', 'X',   1, 'X',   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 'S', 'M', 'X'], # 14
       ['P', 'X',   1, 'X',   1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 'M', 'M', 'M', 'X'], # 15
       ['P',   1,   1, 'X',   1,   1,   1,   1, 'T', 'T', 'T',   1,   1, 'X', 'M', 'M', 'M', 'X'], # 16
       ['P',   1, 'X', 'X', 'X', 'X', 'X', 'H', 'H', 'X', 'X',   1, 'X', 'X', 'X', 'X', 'X', 'X']] # 17

y_len = len(map)-1
x_len = len(map[0])-1
biome = {
    "P": {
        "t": "ERROR",
        "e": True},
    "X": {
        "t": "WOODS",
        "e": True},
    1: {
        "t": "FIELDS",
        "e": False},
    "T": {
        "t": "TOWN CENTRE",
        "e": False},
    "L": {
        "t": "LIEF",
        "e": False},
    "S": {
        "t": "STOLIG",
        "e": False},
    "G": {
        "t": "GALREN",
        "e": False},
    "D": {
        "t": "DISPLACER",
        "e": False},
    "C": {
        "t": "CAVE",
        "e": False},
    "M": {
        "t": "MOUNTAIN",
        "e": True},
    "H": {
        "t": "HILLS",
        "e": True,
    },
    "B": {
        "t": "DRAKE",
        "e": True,
    },
    "o": {
        "t": "PLAYER",
        "e": True,
    }
}

def print_map(map):
    clear()
    draw()
    for column in range(len(map)):
        for row in range(len(map)):
            if map[column][row] == 'X' or 'P':
                map[column][row] = '░'
            elif map[column][row] == 1:
                map[column][row] = ' '
            print(map[column][row], end="")
        print()


e_list = ["Goblin", "Orc", "Fiend", "Celestial", "Ghoul", "Golem", "Ogre"]

mobs = {
    "Goblin": {
        "ehp": 10,
        "eatk": 3,
        'eg': 2
    },
    "Orc": {
        "ehp": 20,
        "eatk": 4,
        'eg': 4
    },
    "Fiend": {
        "ehp": 15,
        "eatk": 2,
        'eg': 5
    },
    "Celestial": {
        "ehp": 45,
        "eatk": 5,
        'eg': 0
    },
    "Ghoul": {
        "ehp": 10,
        "eatk": 3,
        'eg': 7
    },
    "Golem": {
        "ehp": 30,
        "eatk": 7,
        'eg': 10
    },
    "Ogre": {
        "ehp": 25,
        "eatk": 6,
        'eg': 15
    },
    "Drake": {
        "ehp": 100,
        "eatk": 15,
        'eg': 100
    },
}
# current_tile = map[x][y]
# print(current_tile)
# name_of_tile = biome[current_tile]["t"]
# print(name_of_tile)
# enemy_tile = biome[current_tile]["e"]
# print(enemy_tile)

def clear():
    os.system("cls")

def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(PTN),
        str(ELX),
        str(GLD),
        str(HGR),
        str(FOOD),
        str(x),
        str(y),
        str(key)
    ]

    file = open("load.txt", "w")

    for item in list:
        file.write(item + "\n")
    file.close()

def heal(amount):
    global HP
    if HP + amount < HPMAX:
        HP += amount
    else:
        HP = HPMAX

def battle():
    global boss, fight, play, run, HP, PTN, ELX, GLD

    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Drake"
    ehp = mobs[enemy]["ehp"]
    ehpmax = ehp
    eatk = mobs[enemy]["eatk"]
    eg = mobs[enemy]["eg"]

    while fight:
        clear()
        draw()
        print("Defeat the " + enemy)
        draw()
        print(enemy + "'s Health: " + str(ehp) + "/" + str(ehpmax))
        print(name + "'s Health: " + str(HP) + "/" + str(HPMAX))
        print("Potions: " + str(PTN))
        print("Elixers: " + str(ELX))
        draw()
        print("1 - Attack")
        if PTN > 0:
            print ("2 - Use Potion (30HP)")
        if ELX > 0:
            print ("3 - Use Elixer (50HP)")
        draw()

        choice = input("# ")

        if choice == "1":
            ehp -= ATK
            print("You dealt " + str(ATK) + " damage to the " + enemy + ".")
            if ehp > 0:
                HP -= eatk
                print("You took " + str(eatk) + " damage from the " + enemy + ".")
            input("> ")

        elif choice == "2":
            if PTN > 0:
                PTN -= 1
                heal(30)
                HP -= eatk
                print("You took " + str(eatk) + " damage from the " + enemy + ".")
            else: 
                print("You do not have any potions.")
            input("> ")
        elif choice == "3":
            if ELX > 0:
                ELX -= 1
                heal(50)
                HP -= eatk
                print("You took " + str(eatk) + " damage from the " + enemy + ".")
            else: 
                print("You do not have any elixers.")
            input("> ")

        if HP <= 0:
            print("You were killed by the " + enemy + "...")
            draw()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")
        
        if ehp <= 0:
            print("You defeated the " + enemy + ".")
            draw()
            fight = False
            GLD += eg
            print("You've found " + str(eg) + " gold.")
            if random.randint(0, 100) < 25:
                PTN += 1
                print("You've found a potion.")
            if random.randint(0, 100) < 5:
                ELX += 1
                print("You've found an elixer.")
                if enemy == "Drake":
                    print("It's not over")
                    boss = False
            input("> ")
            clear()

def lief():
    global trade_lief, GLD, PTN, ELX, ATK

    while trade_lief:
        clear()
        draw()
        print("Hello traveler, I'm Lief. How can I help you?")
        draw()
        print("Gold: " + str(GLD))
        print("Potions: " + str(PTN))
        print("Elixers: " + str(ELX))
        print("Attack: " + str(ATK))
        draw()
        print("1 - Buy Potion (30HP): 5 Gold")
        print("2 - Buy Elixer (50HP): 10 Gold")
        print("3 - Upgrade Weapon (+2 ATK): 15 Gold")
        print("4 - *Leave*")
        draw()

        choice = input("# ")
        if choice == "1":
            if GLD >= 5:
                PTN += 1
                GLD -= 5
                print("You bought a potion.")
        elif choice == "2":
            if GLD >= 10:
                ELX += 1
                GLD -= 10
                print("You bought an elixer.")
        elif choice == "3":
            if GLD >= 15:
                ATK += 2
                GLD -= 15
                print("You upgraded your weapon.")
        elif choice == "4":
            trade_lief = False

def galren():
    global trade_galren, GLD, PTN, ELX, ATK

    while trade_galren:
        clear()
        draw()
        print("Hello traveler, I'm Galren. How can I help you?")
        draw()
        print("Gold: " + str(GLD))
        print("Potions: " + str(PTN))
        print("Elixers: " + str(ELX))
        print("Attack: " + str(ATK))
        draw()
        print("1 - Buy Potion (30HP): 5 Gold")
        print("2 - Buy Elixer (50HP): 10 Gold")
        print("3 - Upgrade Weapon (+2 ATK): 15 Gold")
        print("4 - *Leave*")
        draw()

        choice = input("# ")
        if choice == "1":
            if GLD >= 5:
                PTN += 1
                GLD -= 5
                print("You bought a potion.")
        elif choice == "2":
            if GLD >= 10:
                ELX += 1
                GLD -= 10
                print("You bought an elixer.")
        elif choice == "3":
            if GLD >= 15:
                ATK += 2
                GLD -= 15
                print("You upgraded your weapon.")
        elif choice == "4":
            trade_galren = False

def stolig():
    global trade_stolig, GLD, PTN, ELX, ATK

    while trade_stolig:
        clear()
        draw()
        print("Hello traveler, I'm Stolig. How can I help you?")
        draw()
        print("Gold: " + str(GLD))
        print("Potions: " + str(PTN))
        print("Elixers: " + str(ELX))
        print("Attack: " + str(ATK))
        draw()
        print("1 - Buy Potion (30HP): 5 Gold")
        print("2 - Buy Elixer (50HP): 10 Gold")
        print("3 - Upgrade Weapon (+2 ATK): 15 Gold")
        print("4 - *Leave*")
        draw()

        choice = input("# ")
        if choice == "1":
            if GLD >= 5:
                PTN += 1
                GLD -= 5
                print("You bought a potion.")
        elif choice == "2":
            if GLD >= 10:
                ELX += 1
                GLD -= 10
                print("You bought an elixer.")
        elif choice == "3":
            if GLD >= 15:
                ATK += 2
                GLD -= 15
                print("You upgraded your weapon.")
        elif choice == "4":
            trade_stolig = False

def displacer():
    global speak, key

    while speak:
        clear()
        draw()
        print("Hello Human, why have you come to me?")
        draw()
        print("1 - Ive come for the key to the dungeon.")
        print("2 - I am lost")
        print("3 - *Leave*")
        draw()

        choice = input("# ")
        if choice == "1":
            if ATK < 15:
                print("You're not strong enough to fight the drake.")
                key = False
            else:
                print("Here is the key, but be warned no traveler has come out of the dungeon alive.")
                key = True
        elif choice == "2":
            print("You are in the great plains east of town, you may find some traders near there to help you on your journey.")
            speak = False
        elif choice == "3":
            speak = False

def draw():
    print("----------------------------------")

def cave():
    global boss, key, fight

    while boss:
        clear()
        draw()
        print("A drake lurks beyond the dungeon doors, What will you do?")
        draw()
        if key:
            print("1 - Use key")
        print("2 - Turn back")

        if choice == "1":
            if key:
                fight = True
                battle()
        elif choice == "2":
            boss = False

def eat(amount):
    global FOOD, HGR
    if FOOD + amount < HGR:
        HGR + amount
    else:
        HGR = HGRMAX

def hunger():
    global fight, play, run, HGR
    if HGR <= 0:
        print("You died of starvation...")
        draw()
        play = False
        run = False
        print("GAME OVER")
        input("> ")
    else:
        HGR -= 1
while run:
    while menu:
        clear()
        draw()
        print("1, NEW GAME")
        print("2, LOAD")
        print("3, RULES")
        print("4, QUIT")
        draw()

        if rules:
            print("I'm the creator of this game and these are the rules.")
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")

        if choice == "1":
            clear()
            name = input("# What is your name? ")
            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 11:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    PTN = int(load_list[3][:-1])
                    ELX = int(load_list[4][:-1])
                    GLD = int(load_list[5][:-1])
                    HGR = int(load_list[6][:-1])
                    FOOD = int(load_list[7][:-1])
                    x = int(load_list[8][:-1])
                    y = int(load_list[9][:-1])
                    key = bool(load_list[10][:-1])
                    clear()
                    print("Welcome Back, " + name + ".")
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Corrupt file")
                    input("> ")
            except OSError:
                print("No loadable file in directory")
                input("> ")
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play:
        save()
        clear()
        if not standing:
            if biome[map[y][x]]["e"]:
                if random.randint(0, 100) <= 30:
                    fight = True
                    battle()
        if play:
            print_map(map)
            draw()
            # print("LOCATION: " + biome[map[y][x]]["t"])
            draw()
            print("Name: " + name)
            print("Health: " + str(HP) + "/" + str(HPMAX))
            print("Hunger: " + str(HGR))
            print("Attack: " + str(ATK))
            print("Potions: " + str(PTN))
            print("Elixers: " + str(ELX))
            print("Gold: " + str(GLD))
            print("Coordinates: ", x,y)
            draw()
            print("0 - SAVE AND QUIT")
            if y > 0:
                print("W - North")
            if x > 0:
                print("A - West")
            if y < y_len:
                print("S - South")
            if x < x_len:
                print("D - East")
            if PTN > 0:
                print("1 - Use Potion (30HP)")
            if ELX > 0:
                print("2 - Use Elixer (50HP)")
            if FOOD > 0:
                print("3 - Eat food (50HGR)")
            if map[y][x] == "L" or map[y][x] == "S" or map[y][x] == "G" or map[y][x] == "D" or map[y][x] == "C":
                print("4 - Enter")
            draw()

            dest = input("# ")

            if dest == "0":
                play = False
                menu = True
                save()
            elif dest == "w":
                if y > 0:
                    y -= 1
                    standing = False
                    hunger()
            elif dest == "d":
                if x < x_len:
                    x += 1
                    standing = False
                    hunger()
            elif dest == "s":
                if y < y_len:
                    y += 1
                    standing = False
                    hunger()
            elif dest == "a":
                if x > 0:
                    x -= 1
                    standing = False
                    hunger()
            elif dest == "1":
                if PTN > 0:
                    PTN -= 1
                    heal(30)
                else: 
                    print("You do not have any potions.")
                input("> ")
                standing = True
            elif dest == "2":
                if ELX > 0:
                    ELX -= 1
                    heal(50)
                else: 
                    print("You do not have any elixers.")
                input("> ")
                standing = True
            elif dest == "3":
                if FOOD > 0:
                    FOOD -= 1
                    eat(50)
                else: 
                    print("You do not have any food.")
                input("> ")
                standing = True
            elif dest == "4":
                if map[y][x] == "L":
                    trade_lief = True
                    lief()
                if map[y][x] == "G":
                    trade_galren = True
                    galren()
                if map[y][x] == "S":
                    trade_stolig = True
                    stolig()
                if map[y][x] == "D":
                    speak = True
                    displacer()
                if map[y][x] == "C":
                    boss = True
                    cave()
            else:
                standing = True
