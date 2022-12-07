
def battleStart(player,monster):
    print("""
     __________________________________________________
    |                            {monsterName}         |
    |                            {monsterHP}           |
    |                                                  |
    |                                                  |
    |                                                  |
    | {playerName}                                     |
    | {playerHP}                                       |
    |                                                  |
    |__________________________________________________|
    """.format(playerName = player.name,playerHP = player.health, monsterName = monster.name,monsterHP=monster.health))