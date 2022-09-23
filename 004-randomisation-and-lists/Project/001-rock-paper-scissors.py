import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
choicesStr = ["rock", "paper", "scissors"]

yourChoice = input("What do you choose: 0 for rock, 1 for paper, 2 for scissors")
yourChoice = int(yourChoice)

aiChoice = random.randint(0,2)

print("Your choice:\n")
print(choices[yourChoice])

print("AI choice:\n")
print(choices[aiChoice])

if choicesStr[yourChoice] == choicesStr[aiChoice]:
    print("Even")
elif choicesStr[yourChoice] == "rock" and choicesStr[aiChoice] == "paper":
    print("You win")
elif choicesStr[yourChoice] == "rock" and choicesStr[aiChoice] == "scissors":
    print("AI wins")
elif choicesStr[yourChoice] == "paper" and choicesStr[aiChoice] == "scissors":
    print("AI win")
elif choicesStr[yourChoice] == "paper" and choicesStr[aiChoice] == "rock":
    print("You win")
elif choicesStr[yourChoice] == "scissors" and choicesStr[aiChoice] == "rock":
    print("AI win")
elif choicesStr[yourChoice] == "scissors" and choicesStr[aiChoice] == "paper":
    print("You win")
else:
    print("Error")
