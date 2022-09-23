# Love counter program - Compares if two names are a match
true_string = "TRUE"
love_string = "LOVE"

person1_name = input("Name 1: ").upper()
person2_name = input("Name 2: ").upper()

love_counter1 = 0
true_counter1 = 0

love_counter2 = 0
true_counter2 = 0


for character1 in person1_name:
    for character2 in love_string:
        if character1 == character2:
            love_counter1 += 1

for character1 in person2_name:
    for character2 in love_string:
        if character1 == character2:
            love_counter2 += 1

total_love = love_counter1 + love_counter2

for character1 in person1_name:
    for character2 in true_string:
        if character1 == character2:
            true_counter1 += 1

for character1 in person2_name:
    for character2 in true_string:
        if character1 == character2:
            true_counter2 += 1

total_true = true_counter1 + true_counter2

score = str(total_love) + str(total_true)
score = int(score)

if score < 10 and score > 90:
    print(f"Your score is **{score}**, you go together as coke and mentos")
elif score <= 50 and score >= 40:
    print(f"Your score is **{score}**, you are alright together")
else:
    print(f"Your score is {score}")
