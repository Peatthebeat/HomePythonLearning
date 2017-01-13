# This is a program to list all cards in a deck in a random sort
import random
import time
# init tuples
import time
numbers = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
cardtype = ('Spades', 'Clubs', 'Hearts', 'Diamond')


def initdeck():                                     # Deck creation function
    for i in range(0, len(numbers)):
        for j in range(0, len(cardtype)):
            global deck
            if i == 0:
                deck = []
            deck.append(numbers[i] + ' of ' + cardtype[j])



def printcards():                                   # Prints whole deck at random
    while len(deck) >= 0:
        randomnumber = random.randint(0, (len(deck) - 1))
        print(deck[randomnumber])
        cardtoremove = (deck[randomnumber])
        deck.remove(cardtoremove)
        time.sleep(0.25)
        if (len(deck) - 1) == 0:
            print(deck[0])
            cardtoremove = (deck[randomnumber])
            deck.remove(cardtoremove)
            break                                   # if import sys, we could use sys.exit() instead
        time.sleep(0.002)                           # but program would terminate without anything else


# Main Section
initdeck()
printcards()
print('done!')
