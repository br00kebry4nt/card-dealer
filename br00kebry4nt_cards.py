import random

NUMCARDS = 52
RANKNAME = ("Ace", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King")

SUITNAME = ("clubs", "hearts", "spades", "diamonds")
HANDS = ("deck", "player", "computer")

DECK = 0
PLAYER = 1
COMPUTER = 2
    
def initCards():
    return [DECK] * NUMCARDS

def showDB(cardDB):
    for cardNum, location in enumerate(cardDB):
        print(f"{cardNum:3}: {getCardName(cardNum):25} {HANDS[location]}")
    print()
    
def getCardName(cardNum):
    suit = cardNum // 13
    rank = cardNum % 13
    return f"{RANKNAME[rank]} of {SUITNAME[suit]}"

def assignCard(cardDB, hand):
    unassignedCards = [i for i, location in enumerate(cardDB) if location == DECK]
    if unassignedCards:
        cardNum = random.randint(0, len(unassignedCards) - 1)
        cardDB[unassignedCards[cardNum]] = hand
        
def showHand(cardDB, hand): 
    print(f"Cards in {HANDS[hand]} hand:")
    for cardNum, location in enumerate(cardDB):
        if location == hand:
            print(f"{getCardName(cardNum)}")
    print()

def main():
    cardDB = initCards()

    for i in range(5):
        assignCard(cardDB, PLAYER)
        assignCard(cardDB, COMPUTER)

    showDB(cardDB)

    showHand(cardDB, PLAYER)
    showHand(cardDB, COMPUTER)
    
main()      