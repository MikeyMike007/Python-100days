import random
import art
import time
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

def drawCard(cardDeck,numberOfCardsToDraw,theHand):
    for cardNumber in range(0,numberOfCardsToDraw):
        card = random.choice(list(cardDeck.keys()))
        theHand.append(card)

def sumCards(cardsInHand):
    result=0
    results=[]
    for card in cardsInHand:
        result += cards[card]

    if "Ace" not in cardsInHand:
        results.append(result)
        return results
    
    else:
        results.append(result)
        result = result - cards["Ace"] + cards["One"]
        results.append(result)
        return results


def printResult(hand, user):
    result = sumCards(hand)
    if "Ace" in hand:
        print(f"Result of {user} is: {result[0]} or {result[1]}")
    else:
        print(f"Result of {user} is: {result[0]}")

def hasBlackJack(results):
    blackJack = 21
    if blackJack in results:
        return True
    else:
        return False

def compare(userResult, aiResult):
    
    if userResult > aiResult:
        print("You win")
    elif userResult < aiResult:
        print("AI Wins")
    else:
        print("Equal")
    
cards = {
    "Ace": 11,
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "King": 10,
    "Queen": 10
}

def BlackJack():

    ai = "*AI*"
    user = "*User*"
    userHand = []
    aiHand = []

    drawAnotherCard = True

    drawCard(cards, 2, userHand)
    userResult = sumCards(userHand)

    drawCard(cards, 2, aiHand)
    aiResult = sumCards(aiHand)

    print(art.logo)

    print("Drawing two cards for user...")
    time.sleep(1)
    print(f"Users hand is: {userHand}")
    printResult(userHand,user)
    time.sleep(1)
    print("\n")
    print("\n")
    
    print("Drawing two cards for AI...")
    time.sleep(1)
    print(f"AI hand is: {aiHand}")
    printResult(aiHand,ai)
    time.sleep(1)
    print("\n")
    print("\n")

    while drawAnotherCard:

        if hasBlackJack(userResult):
            print(f"User has BlackJack..... You win!\n")
            playAgain = input("Do you want to play again")
            if playAgain == "y":
                BlackJack()
            else:
                exit()
        

        if hasBlackJack(aiResult):
            print(f"AI has BlackJack... You loose\n")
            playAgain = input("Do you want to play again")
            if playAgain == "y":
                BlackJack()
            else:
                exit()

        if all(result > 21 for result in userResult):
            print(f"Your result is over 21")
            printResult(userHand,user)
            playAgain = input("Do you want to play again")
            if playAgain == "y":
                BlackJack()
            else:
                exit()

        answer= input("Do you want to drae another card (y/n):  ")
        if answer == "y":
            print("Drawing one cards for user...")
            drawCard(cards, 1, userHand)
            userResult = sumCards(userHand)
            time.sleep(1)
            print(f"Users hand is: {userHand}")
            printResult(userHand,user)
        else:
            drawAnotherCard = False
    
    
    while all(result < 17 for result in aiResult):
        print("Drawing one cards for AI...")
        drawCard(cards, 1, aiHand)
        aiResult = sumCards(aiHand)
        time.sleep(1)
        print(f"AI hand is: {aiHand}")
        printResult(aiHand,ai)

    if min(aiResult) > 21:
        print("You win....")
    else:
        compare(userResult,aiResult)

BlackJack()