import art

bidBook = {}

print(art.logo)

newBidders = True

while newBidders is True:
    name = input("Please enter your name: ")
    bidPrice = int(input("Please enter your bid price: "))
    bidBook[name] = bidPrice
    print(f"{name} bid added at {bidPrice}...")
    question = input("Is there another bidder (y/n")
    if question == "n":
        newBidders = False

maxBid = max(bidBook.values())
maxKey = max(bidBook, key=bidBook.get)
print(f" Max bid is {maxBid} won by {maxKey}")


