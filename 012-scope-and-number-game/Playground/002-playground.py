game_level = 3
enemies = ["skeleton", "zombie", "alien"]
game_level = 3

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]


#Error - variable new_enemy out of scope
print(new_enemy)