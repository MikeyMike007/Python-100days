# Control flow and logical operators

| Operator | Meaning               |
| -------- | --------------------- |
| `>`      | Greater than          |
| `<`      | Less than             |
| `>=`     | Greater than or equal |
| `<=`     | Less than or equal    |
| `==`     | Equal to              |
| `!=`     | Not equal to          |

## Control flow with if, else and conditional operators

Example with if and else

```py
print("Welocme to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height > 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry, you have to grow taller before you can ride")
```

## Nested if statements and elif statements

Following code illustrates a typical if/elif/else snippet

```python
if condition1:
  do A
elif condition2:
  do B
else:
  do C
```

An example

```py
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?: "))
    if age < 12:
        print("Teh ticket is 5 dollar")
    elif age >= 12 and age < 18:
        print("The ticket is 7 dollar")
    else:
        print("The ticket is 12 dollar")
else:
    print("Sorry, you have to grow taller before you can ride")
```

## Multiple if statement

Multiple if statements can be illustrated by following code

```python
if condition1:
  do A
if condition2:
  do B
if condition3:
  do C
```

An example

```py
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?: "))
    if age < 12:
        bill = 5
        print(f"The ticket is {bill} dollar")
    elif age >= 12 and age < 18:
        bill = 7
        print(f"The ticket is {bill} dollar")
    else:
        bill = 12
        print(f"The ticket is {bill} dollar")

    wants_photo = input("Do you want a photo (y/n)")
    if wants_photo == "y":
        bill += 3
        186

    print(f"your final bill is {bill} dollar")
else:
    print("Sorry, you have to grow taller before you can ride")
```

## Logical operators

| Logical operators |
| ----------------- |
| `A and B`         |
| `C or D`          |
| `not E`           |

An example

```python
print("Welocme to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?: "))
    if age < 12:
        bill = 5
        print(f"The ticket is {bill} dollar")
    elif age >= 12 and age < 18:
        bill = 7
        print(f"The ticket is {bill} dollar")
    elif age >= 45 and age <= 55:
        bill = 0
        print(f"The ticket is {bill} dollar")
    else:
        bill = 12
        print(f"The ticket is {bill} dollar")

    wants_photo = input("Do you want a photo (y/n)")
    if wants_photo == "y":
        bill += 3
        186

    print(f"your final bill is {bill} dollar")
else:
    print("Sorry, you have to grow taller before you can ride")
```

