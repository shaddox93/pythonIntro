#!/usr/bin/env python
# Dave Reed
# CS160

#----------------------------------------------------------------------

import random

#----------------------------------------------------------------------

class CardDeck:

    'class for representing a deck of cards as the numbers 0 through 51'

    #------------------------------------------------------------------

    def __init__(self):
        
        '''create a deck of cards represented by numbers 0-51'''
        
        self.init()

    #------------------------------------------------------------------
    
    def init(self):

        '''orders the cards from 0 to 51 and sets next card to be dealt
        to card 0'''
        
        self.cards = list(range(52))
        self.pos = 0

    #------------------------------------------------------------------

    def shuffle(self):

        '''shuffles all 52 cards'''

        # for each card in the deck
        for i in range(52):
            # pick a random card to swap it with
            r = random.randrange(0, 52)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    #------------------------------------------------------------------

    def dealOne(self):

        '''returns the number corresponding to the next card;
        returns None if there are no cards left to be dealt'''
        
        # if cards left to deal
        if self.pos < 52:
            # get card and update the next card to deal
            c = self.cards[self.pos]
            self.pos = self.pos + 1
            return c
        else:
            return None

#----------------------------------------------------------------------
