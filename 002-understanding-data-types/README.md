# Understanding data types

```py
# prints 'H'
print("Hello"[0])

# concatenates the figures in the strings into "123345"
print("123" + "345")

# adds figures
print(123 + 456) # Treats figures as numbers and adds them

```

Some examples on datatypes

Integer: 1,2,3,4,5\
Float: 3.14123\
Boolean: True, False

## Type error, type checking and type conversion

Following code gives a type error since the variable `num_char` is an integer and not a string.

```py
num_char = len(input("Your name "))
print("your name has " + num_char + " characters")

```

What you need to do in order to run the code above is to convert the integer to a string:

```py
num_char = len(input("Your name "))
print("your name has " + str(num_char) + " characters")
```

Some code examples:

```py
# prints 170.5 which is a float
print(70+float("100.5"))

# prints 70100. Since they are strings, they will be concatenates with the + operator.
print(str(70)+str(100))

# Prints the data type which is a float
a = float(123)
print(type(a))
```

## Mathematical operations in python

```py
# The power function i.e. 2^4 = 2 * 2 * 2 * 2 = 16
print(2 ** 4)

# Prints a float. Division always gives the type float
print(type(10 / 2 ))
```

## Number manipulation and F strings in python

```py
# Prints 2.
print(8 // 3)

# Prints Int
print(type(8 // 2))
```

```py
score = 100

score *= 2 # score is now 200
score /= 2 # score is now 100 again
score += 2 # score is now 102
score -= 2 # score is now 100
```

```py

# Following code illustrates how F-strings works
score=100
height=1.86
isWinning = True

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
```
