################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}") # prints 2

increase_enemies()
print(f"enemies outside function: {enemies}") # prints 1

#-------------------------------------------------
# Local scope
def drink_potion():
    # potion_strenght only has a local scope
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strenght) # Error!! cannot be accessed
#-------------------------------------------------


#-------------------------------------------------
#Global scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
#-------------------------------------------------