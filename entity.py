import random


class Player:
    def __init__(self, playerName):
        self.name = playerName
        self.health = 100
        self.level = 1
        self.xp = 0

    def updateHealth(self,healthDamage):
        if healthDamage >= self.health:
            print("You are dead {name}".format(name=self.name))
            quit()
        else:
            self.health = self.health - healthDamage

    def updateExperience(self,roughXP):
        self.xp += roughXP

        if self.xp <= 100:
            self.level + 1
            self.xp - 100


           



class Monster:

    def __init__(self, health, level, name,difficulty):
        self.health = health
        self.level = level
        self.name = name
        self.difficulty = difficulty


    def updateHealth(self,healthDamage):
        if healthDamage >= self.health:
            print("{name} has slain the {monName}".format(name=playerCharacter.name,monName=self.name))
            quit()
        else:
            self.health = self.health - healthDamage

    def dead(self):
       playerCharacter.updateExperience(self.level)
    
                



def monsterGenerator():
    monsterQualities = {"Cute":0,"Slow":1,"Tiny":3,"Normal":4,"Huge":5,"Angry":6,"Vicious":7,"Deadly":8}
    monsterTypes = {"Pig":0,"Bat":1,"Bear":2,"Slime":3,"Goblin":4,"Dwarf":5,"Elf":6,"Orc":7,"Dragon":8,"Beholder":9}

    monQuality = random.choice(list(monsterQualities.keys()))
    monType = random.choice(list(monsterTypes.keys()))
    monDifficulty = (monsterQualities[monQuality] + monsterTypes[monType])
    monName = monQuality + ' ' + monType
    monLevel = random.choice(range(playerCharacter.level,playerCharacter.level+monDifficulty))
    monHealth = playerCharacter.level * (1 + monDifficulty +  random.choice(range(1, 80)))
    if monLevel == 0:
        monLevel = 1
    return Monster(monHealth,monLevel,monName,monDifficulty)



def playerGenerator():
    global playerCharacter
    playerName = input("What is your name? \n\n")
    playerCharacter = Player(playerName)
    return playerCharacter








    

