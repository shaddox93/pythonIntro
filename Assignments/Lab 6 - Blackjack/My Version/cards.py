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

def main():

    # open a graphing window
    win = GraphWin('Cards', 600, 400)

    # create a card deck (d) and shuffle it
    d = CardDeck()
    d.shuffle()

    # score determines blackjack score
    score1 = 0
    score2 = 0
    # place determines where cards are drawn
    place1 = 100
    place2 = 100
    # loop deals and prints both players cards to the screen and determine's player's scores
    for i in range(6):
        c = d.dealOne()
        value, filename = cardInfo(c)
        # draws player 1's card and determines player 1's score
        if i <= 2:
            drawCard(filename, place1, 100, win)
            place1 = place1 + 100
            score1 = score1 + value
        # draws player 2's card and determine's player 2's score
        else:
            drawCard(filename, place2, 300, win)
            place2 = place2 + 100
            score2 = score2 + value

    # draws player 1's score if they didn't bust
    if score1 <= 21:
        p1score = Text(Point(400, 100),'Total: ' + str(score1))
        p1score.draw(win)
    # draws 'busted' if player 1's score is over 21
    else:
        busted = Text(Point(400, 100), 'Busted')
        busted.draw(win)

    # draws player 2's score if they didn't bust
    if score2 <= 21:
        p2score = Text(Point(400, 300),'Total: ' + str(score2))
        p2score.draw(win)
    # draws 'busted if player 2's score is over 21
    else:
        busted = Text(Point(400, 300), 'Busted')
        busted.draw(win)

    # player 1 wins if:
    #   score1 is greater than score2 and is less than or equal to 21 or
    #   score2 is greater than 21 and score1 is less than or equal to 21
    if score1 > score2 and score1 <= 21 or score2 > 21 and score1 <= 21:
        outcome = Text(Point(300, 375), 'Player 1 Wins!')
        outcome.draw(win)

    # player 2 wins if:
    #   score2 is greater than score1 and is less than or equal to 21 or
    #   score1 is greater than 21 and score2 is less than or equal to 21
    elif score2 > score1 and score2 <= 21 or score1 > 21 and score2 <=21:
        outcome = Text(Point(300, 375), 'Player 2 Wins!')
        outcome.draw(win)

    # players tie if both scores are equal to each other and less than or equal to 21
    elif score1 == score2 and score1 <= 21 and score2 <= 21:
        outcome = Text(Point(300, 375), 'Tie')
        outcome.draw(win)

    # handles situation in which both players' scores are over 21
    elif score1 > 21 and score2 > 21:
        outcome = Text(Point(300, 375), 'Both Players Busted')
        outcome.draw(win)

    # wait for mouse click and close window
    win.getMouse()
    win.close()
        
#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
