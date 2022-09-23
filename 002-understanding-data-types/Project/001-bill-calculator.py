# following script calculates how much each person should pay from a bill
print("Welcome to the tip calculator")

bill=int(input("Input your total bill: $"))
tip = int(input("what percentage of tip do you want to give "))
people = int(input("how many people "))
pay = round(bill * (1 + tip / 100) / people,2)

print(f"Each person should pay ${pay}")
