#----------------------------------------------------------------------
# PokerHand.py
# Victor Stasek
# 11/28/2012
#----------------------------------------------------------------------

from CardDeck import *
import sys

#----------------------------------------------------------------------

class PokerHand:

    '''class for representing a poker hand''' 
    # Poker value of hands in increasing order so they can be compared
    HIGH_CARD = 0
    TWO_OF_A_KIND = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8

    # hand names for printing the card names
    HAND_NAMES = ('High Card', 'Two of a Kind', 'Two Pairs', 'Three of a Kind',
                 'Straight', 'Flush', 'Full House', 'Four of a Kind',
                 'Straight Flush')

    
    #------------------------------------------------------------------

    def __init__(self):

        '''initialize empty hand'''

        self.cards = []

    #------------------------------------------------------------------

    def addCard(self, cardNumber):

        '''add cardNumber to the hand'''

        self.cards.append(cardNumber)

    #------------------------------------------------------------------

    def straight(self, face):
        
        pos = face.index(1)
        for i in range(4):
            newpos = face.index(1, pos+1)
            pos = newpos
            
        pos = face.index(1)
        
        if newpos == pos + 4:
            return True
        else:
            return False
        
    #------------------------------------------------------------------

    def evalHand(self):


        '''determine the value of the hand and return a tuple; the
        first value in the tuple is an integer corresponding to the
        hand value using the constants HIGH_CARD, TWO_OF_A_KIND, etc.;
        the remaining values in the tuple depend on the type of hand
        and are described below to break ties based on the face values
        of the cards

        for HIGH_CARD, it is five values: the face values sorted in
        descending order
        
        for TWO_OF_A_KIND, it is four values: the face value for the
        pair, followed by the face values of the other cards in
        descending order

        for TWO_PAIRS, it is three values: the face value of the
        higher pair, the face value of the lower pair, followed by the
        face value of the other card
        
        for THREE_OF_A_KIND, it is three values: the face value of the
        three of a kind, followed by the face value of the other two
        cards in descending order
        
        for STRAIGHT, it is one value: the face value of the lowest
        card in the straight
        
        for FLUSH, it is five values: the face values sorted in
        descending order

        for FULL_HOUSE, it is two values: the face value of the three
        of a kind, followed by the face value of the pair

        for FOUR_OF_A_KIND, it is two values: the face value that
        there are four of followed by the face value that there is one
        of

        for STRAIGHT_FLUSH, it is one value: the face value of the
        lowest card in the straight'''

        face = [0] * 13
        suit = [0] * 4

        for c in self.cards:
            f = c % 13
            s = c // 13
            face[f] += 1
            suit[s] += 1

        if face.count(1) == 5:

            straight = self.straight(face)

            # Straight Flush
            if suit.count(5) == 1 and straight == True:
                sFValue = face.index(1) + 1
                print(sFValue)
                return self.STRAIGHT_FLUSH

            # Straight
            elif straight == True:
                return self.STRAIGHT

            # Flush
            elif suit.count(5) == 1 and straight == False:
                return self.FLUSH

            # High Card
            else:
                hcList = []
                pos = face.index(1)
                hcValue = pos + 1
                hcList.append(hcValue)
                for i in range(4):
                    pos = face.index(1, pos + 1)
                    hcValue = pos + 1
                    hcList.append(hcValue)
                hcList.sort()
                hcList.reverse()
                print(hcList)
                return self.HIGH_CARD

        # Four of a Kind
        elif face.count(4) == 1:
            return self.FOUR_OF_A_KIND

        # Full House
        elif face.count(3) == 1 and face.count(2) == 1:
            return self.FULL_HOUSE

        # Three of a Kind
        elif face.count(3) == 1:
            return self.THREE_OF_A_KIND

        # Two Pairs
        elif face.count(2) == 2:
            return self.TWO_PAIRS

        # Two of a Kind
        elif face.count(2) == 1:
            return self.TWO_OF_A_KIND

#----------------------------------------------------------------------

def main():
##    hand = PokerHand()
##    d = CardDeck()
##    d.shuffle()
##
##    for i in range(5):
##        c = d.dealOne()
##        hand.addCard(c)
##
##    r = hand.evalHand()
##    
##    print(r)
##    print(PokerHand.HAND_NAMES[r])
    pass

#----------------------------------------------------------------------

if __name__ == '__main__':
    main()
