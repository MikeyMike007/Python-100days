import random
bankerNames = input("What is your names (comma separated): ")
bankerNames =   bankerNames.split(", ")

payingBankerID = random.randint(0,len(bankerNames)-1)
payingBankerName = bankerNames[payingBankerID]

print(f"{payingBankerName} is going to pay the bill")

