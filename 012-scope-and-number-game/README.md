# Scope

Example

```python
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}") # prints 2

increase_enemies()
print(f"enemies outside function: {enemies}") # prints 1

# Local scope
def drink_potion():
    # potion_strenght only has a local scope
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strenght) # Error!! cannot be accessed

# Global scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()

```

OK:

```py
game_level = 3
enemies = ["skeleton", "zombie", "alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)
```

NOT OK:

```py
enemies = ["skeleton", "zombie", "alien"]
game_level = 3

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]


# Error - variable new_enemy out of scope
print(new_enemy)

```

## How to modify a global variable

Please note that the variables enemies within the increase_enemies function and outside the same function are two totally different variables:

```python
# Modifying global scope
enemies = "Skeleton"

def increase_enemies():
  enemies = "Zombie"
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# prints:
# Enemies inside function: Zombie
# Enemies outside function: Skeleton
#
# Please note that the variables are two totally different variables,
# Even as they have the same name
```

Note that you should never use the same name on a local and global variable

Note that following code gives the following error `local variable 'enemies' referenced before assignment`

```python
# Modifying global scope
enemies = 1

def increase_enemies():
  enemies += 1
  print(f"enemies inside function: {enemies}") # prints 2

increase_enemies()
print(f"enemies outside function: {enemies}") # prints 1

```

You need to define a variable as a global if you would like the code above work:

```py
# Modifying global scope

enemies = 1

def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}") # prints 2

increase_enemies()
print(f"enemies outside function: {enemies}") # prints 1
```

Avoid global variables. You can use it, but don’t try to modify it.

## Python constants and global scope

Praxis is to define variables as globals but then use the syntax that state them in upper case letters:

```python
# Defining global variables
# Should be stated with upper cases:

PI = 3.14159
URL ="http://www.google.com"
TWITTER_HANDLE = "@myTwitterhandle"

```

