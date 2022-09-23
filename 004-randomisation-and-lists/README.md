# Randomisation and python list

## Random module

```py
import random

random_integer = random.randint(1,10)
print(random_integer)


#0.0000000 - 0.9999999
random_float = random.random() * 5
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")
```

## Understanding the offset and appending items to a list

```py
myList = ["Delaware","Pennsylvania","New Jersey"]

# Printing list items

print(myList[0])
print(myList[1])
print(myList[2])


# Print list items from the end
print(myList[-1])
print(myList[-2])
print(myList[-3])

# Updating list items

myList[0] = "New Delaware"

print(myList[0])

# Append a list

myList.append("D Land")
print(myList)

# Extend a list

myList.extend(["A land","B land", "C land"])
print(myList)
```

