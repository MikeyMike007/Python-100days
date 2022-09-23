# Uses f strings to display if a year is a leap year
year = int(input("Which year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a leap year")
        else:
            print(f"The year {year} is a not leap year")
    else:
         print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is a not leap year")


