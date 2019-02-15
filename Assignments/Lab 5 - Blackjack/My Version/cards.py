#!/usr/bin/env python
# Dave Reed
# CS160

#-----------------------------------------------------------------------

import os

from graphics import *
from CardDeck import *

#-----------------------------------------------------------------------

def drawCard(filename, x, y, window):

    '''draw image specified by filename centered at (x, y) in window'''

    p = Point(x, y)
    prefixes = ['cardset/', '../cardset/', './']
    for prefix in prefixes:
        fname = '{}{}'.format(prefix, filename)
        try:
            image = Image(p, fname)
            image.draw(window)
            break
        except:
            pass

#-----------------------------------------------------------------------

def cardInfo(number):
    
    '''returns the blackjack value and and filename for card specified
    by cardNumber

    0-12 are the Ace-King of clubs
    13-25 are the Ace-King of spades
    26-38 are the Ace-King of hearts
    39-51 are the Ace-King of diamonds
    
    the blackjack value for the cards 2-9 are the corresponding
    number; 10, Jack, Queen, and King all have blackjack values of 10
    and an Ace has a value of 11
    
    filename is of the form: ##s.gif
    where ## is a two digit number (leading 0 if less than 10)
    and s is a letter corresponding to the suit value
    c for clubs, s for spades, h for hearts, d for diamonds'''

    # divides the 52 cards into four equal sets of 13 numbered 0 - 3
    suit = number // 13
    
    # assigns specific suit to card    
    if suit == 0:
        x = 'c'
    elif suit == 1:
        x = 's'
    elif suit == 2:
        x = 'h'
    elif suit == 3:
        x = 'd'
        
    # divides the 52 cards into four equal sets of 13 numbered 1 - 13
    fnumber = (number % 13) + 1

    # puts everything gathered so far together to form file name
    fname = ('{:02}'.format(fnumber) + x + '.gif')

    # assigns specific blackjack value to card
    if fnumber == 1:
        bjValue = 11 # Ace
    elif fnumber >= 11:
        bjValue = 10 #Jack, Queen, King
    else:
        bjValue = fnumber # 2 - 10
    
    return bjValue, fname

#-----------------------------------------------------------------------

def main():
    
    #win = GraphWin('Cards', 600, 400)
    
    # delete this next line - just here to show you drawing a specific card
    #drawCard('11h.gif', 100, 100, win)

    #for i in range(52):
    #    fname, bjValue = cardInfo(i)
    #    print(fname, bjValue)
        
    # wait for mouse click and close window
    #win.getMouse()
    #win.close()

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
