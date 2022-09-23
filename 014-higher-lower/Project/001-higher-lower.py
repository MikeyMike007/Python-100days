import os
import art
import game_data
import random
import time

logo = art.logo
vs = art.vs
data = game_data.data
score = 0
isGame = True

def getDataPoint():
    return random.choice(data)

def presentDataPoint(dataPoint,option):
    name = dataPoint["name"]
    follower_count = dataPoint["follower_count"]
    description = dataPoint["description"]
    country = dataPoint["country"]
    print(f"Option {option}: {name}, a {description} from {country}")

def presentVS():
    print("\n")
    print(vs)
    print("\n")

while isGame:

    accountA = getDataPoint()
    accountB = getDataPoint()

    while accountA == accountB: 
        accountB = getDataPoint()

    os.system("Clear")
    time.sleep(1)
    presentDataPoint(accountA,'A')
    time.sleep(1)
    presentVS()
    time.sleep(1)
    presentDataPoint(accountB,'B')
    print("\n")
    choice = input("Choose: A or B: ")

    if choice == "A":
        if accountA["follower_count"] > accountB["follower_count"]:
            score += 1
            print(f"Right guess, your score is {score}")
            time.sleep(2)
        else:
            print(f"Wrong answer, you loose with score {score}")
            isGame = False
            time.sleep(2)
    elif choice == "B":
        if accountA["follower_count"] < accountB["follower_count"]:
            score += 1
            print(f"Right guess, your score is {score}")
            time.sleep(2)
        else:
            print(f"Wrong answer, you loose with score {score}")
            isGame = False
            time.sleep(2)

