# Pizza order program
size = input("What pizza size do you want to have (S/M/L): ")

if size == "S":
    bill = 15
    peperoni = input("Do you want to have peperoni (Y/N): ")
    if peperoni == "Y":
        bill += 2
    elif peperoni == "N":
        bill += 0
    else:
        print("Unknown answer... quitting")
        quit()
elif size == "M":
    bill = 20
    peperoni = input("Do you want to have peperoni (Y/N): ")
    if peperoni == "Y":
        bill += 3
    elif peperoni == "N":
        bill += 0
    else:
        print("Unknown answer... quitting")
        quit()
    
elif size == "L":
    bill = 25
    peperoni = input("Do you want to have peperoni (Y/N): ")
    if peperoni == "Y":
        bill += 3
    elif peperoni == "N":
        bill += 0
    else:
        print("Unknown answer... quitting")
        quit()

else:
    print("Size unknown")
    exit()

cheese = input("Do you want cheese (Y/N): ")

if cheese == "Y":
    bill += 1
elif cheese =="N":
    bill += 0
else:
    print("Unknown answer...quitting")
    quit()

print(f"Your total bill is {bill}")
`
