################### Scope ####################

#Modifying global scope

enemies = 1

def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}") # prints 2

increase_enemies()
print(f"enemies outside function: {enemies}") # prints 1
