# Estimates if a given year from stdin is a leap year
year = int(input("Which year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year " + str(year) + " is a leap year")
        else:
            print("The year " + str(year) + " is not a leap year")
    else:
         print("The year " + str(year) + " is a leap year")
else:
    print("The year " + str(year) + " is not a leap year")


