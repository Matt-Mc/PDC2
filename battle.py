import random
import time


playerTurn = True


def battleStart(player,monster):
    
    updateBattleState(player,monster,"")   


def battleCycle(player,monster):
    global playerTurn
    if playerTurn == True:
        playerTurn = False
        playerAction(player,monster)
    else:
        playerTurn = True
        monsterAction(player,monster)


def playerAction(player,monster):
    playerAction = input("What Action would you like to take?: \n\n").lower
    
    if playerAction == "attack" or playerAction == "a":
        playerDamage = player.level + random.choice(range(1, 10))
        monster.updateHealth(playerDamage)
        action = "{playerName} hits {monsterName} for {playerDamage}!".format(monsterName = monster.name, playerName = player.name, playerDamage = playerDamage)
        updateBattleState(player,monster,action)



def monsterAction(player,monster):
    time.sleep(3)
    monDamage = monster.level * monster.difficulty / random.choice(range(1, 10))
    player.updateHealth(monDamage)
    action = "{monsterName} hits {playerName} for {monDamage}!".format(monsterName = monster.name, playerName = player.name, monDamage = monDamage)
    updateBattleState(player,monster,action)

def updateBattleState(player,monster,action):
    print("""\n\n\n\n\n\n\n\n
     __________________________________________________
                                 
                                 
                                 {monsterName} 
                                 Lvl: {monsterLevel}         
                                 HP: {monsterHP}           
                                                      
                                                                                              
      {playerName}
      Lvl: {playerLevel}                                     
      HP: {playerHP}                                       

      Actions: Attack                                           
    ___________________________________________________
    {prevAction}
    """.format(playerName = player.name,playerHP = player.health,playerLevel = player.level, monsterName = monster.name,monsterHP=monster.health, monsterLevel=monster.level,prevAction=action))
    
    battleCycle(player,monster)
