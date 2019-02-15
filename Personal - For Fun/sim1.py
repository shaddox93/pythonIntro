from CardDeck import *
from blackjack import cardInfo

n = eval(input('number of games to simulate: '))
for card1 in range(1, 12):

    busts = 0
    for i in range(n):

        # simulate a game starting with card1 as initial value
        deck = CardDeck()
        deck.shuffle()
        total = card1
        while total < 17:
            card = deck.dealOne()
            value, filename = cardInfo(card)
            total += value
        if total > 21:
            busts += 1
    print(card1, '{:6.2f}'.format(busts / n * 100))
    
