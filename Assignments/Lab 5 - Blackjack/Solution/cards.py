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

    # calculate face and suit values
    suitNum = number // 13
    faceNum = number % 13

    value = faceNum + 1
    if value > 10:
        value = 10
    elif value == 1:
        value = 11

    suits = 'cshd'
    # calculate name of file
    # face is a number from 1 to 13 with leading zeros for 1-9
    filename = '{:02}{}.gif'.format(faceNum+1, suits[suitNum])

    return value, filename

#-----------------------------------------------------------------------

def drawThreeCards(deck, startx, y, win):

    '''deals three cards from the CardDeck deck, and displays them in
    a row in the GraphWin win specified by integer y starting at
    integer startx and moving over 100 pixels for each card; returns
    the blackjack total for the three cards'''

    total = 0
    x = startx
    for i in range(3):
        # deal card and draw it
        c = deck.dealOne()
        value, filename = cardInfo(c)
        drawCard(filename, x, y, win)
        # move over 100 pixels for next card
        x += 100
        # accumulate blackjack value of all the cards
        total += value
    return total
        
#-----------------------------------------------------------------------

def main():
    
    win = GraphWin('Cards', 600, 400)
    # create a single card deck and shuffle it
    deck = CardDeck()
    deck.shuffle()

    # draw three cards at y=100
    total1 = drawThreeCards(deck, 100, 100, win)
    # display blackjack value of the cards
    if total1 > 21:
        msg = 'Busted'
    else:
        msg = 'Total: {}'.format(total1)
    Text(Point(400, 100), msg).draw(win)

    # deal three cards at y=250
    total2 = drawThreeCards(deck, 100, 250, win)
    # display blackjack value of the cards
    if total2 > 21:
        msg = 'Busted'
    else:
        msg = 'Total: {}'.format(total2)
    Text(Point(400, 250), msg).draw(win)

    # determine winner
    # if player1 busted
    if total1 > 21:
        if total2 > 21:
            msg = 'Both players busted'
        else:
            msg = 'Player 2 wins'

    # player 1 didn't bust
    else:
        if total2 > 21:
            msg = 'Player 1 wins'
        elif total1 > total2:
            msg = 'Player 1 wins'
        elif total1 == total2:
            msg = 'Tie'
        else:
            msg = 'Player 2 wins'

    # display winner
    Text(Point(200, 350), msg).draw(win)

    # wait for mouse click and close window
    win.getMouse()
    win.close()

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
