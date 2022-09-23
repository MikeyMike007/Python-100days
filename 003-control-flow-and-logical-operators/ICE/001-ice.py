# Following code reads a number from stdin and then checks wether the number is
# even
number = int(input("What number do you want to check "))

if (number % 2) == 0:
    print("The number " + str(number) + " is even")
else:
    print("The number " + str(number) + " is odd")

