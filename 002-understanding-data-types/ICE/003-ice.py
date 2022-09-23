# following code illsutrates f-strings in python
age = input("What is your current age?")

age = int(age)
days = (90-age)*365
weeks = (90-age)*52
months = (90-age)*12

print(f"you have {days} days,  {weeks} weeks, {months} months left")
