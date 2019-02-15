
from CardDeck import *
from blackjack import cardInfo

def main():

    n = eval(input('enter # games: '))
    for card1 in range(1, 12):
        busted = 0
        for i in range(n):

            # simulate game with card1 as initial card
            d = CardDeck()
            d.shuffle()
            total = card1
            while total < 17:
                nextCard = d.dealOne()
                value, filename = cardInfo(nextCard)
                total += value
            if total > 21:
                busted += 1
        print('{:2} {:6.2f}'.format(card1, busted / n * 100))

if __name__ == '__main__':
    main()
    
