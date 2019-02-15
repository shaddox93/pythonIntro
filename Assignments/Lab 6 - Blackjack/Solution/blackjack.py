#!/usr/bin/env python

#----------------------------------------------------------------------
# blackjack.py
# Dave Reed
# 10/30/2011
#----------------------------------------------------------------------

import sys
from graphics import *
from CardDeck import *

#----------------------------------------------------------------------

def drawCard(filename, x, y, window):

    '''draw image specified by filename centered at (x, y) in window'''

    p = Point(x, y)
    prefixes = ['cardset/', '../cardset/', './']
    for prefix in prefixes:
        fname = '{}{}'.format(prefix, filename)
        try:
            image = Image(p, fname)
            image.draw(window)
            return image
        except:
            pass

#----------------------------------------------------------------------

def cardInfo(cardNumber):

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
    c for clubs, s for spades, h for hearts, d for diaomnds'''

    # calculate suit and face numbers
    suitNum = cardNumber // 13
    faceNum = cardNumber % 13

    # calculate blackjack value
    value = faceNum + 1
    if value > 10:
        value = 10
    elif value == 1:
        value = 11

    # calculate name of file
    # face is a number from 1 to 13 with leading zeros for 1-9
    suits = 'cshd'
    filename = '{:>02}{}.gif'.format(faceNum + 1, suits[suitNum])
    return value, filename

#----------------------------------------------------------------------

def createWindow():

    '''create window with hit me button and return the window'''

    win = GraphWin('Blackjack', 800, 600)
    button = Rectangle(Point(650, 100), Point(750, 150))
    button.draw(win)
    hit = Text(Point(700, 125), 'Hit me')
    hit.draw(win)
    return win

#----------------------------------------------------------------------

def aceScore(total, aces):

    '''returned updated score and number of aces counting aces as 1 if
    counting them as 11 causes the score to be over 21'''

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total, aces

#----------------------------------------------------------------------

def displayScore(text, score):

    '''displays the score in the specified text field'''
    
    if score > 21:
        msg = 'busted'
    else:
        msg = str(score)
    text.setText(msg)

#----------------------------------------------------------------------

def processCard(card, win, posX, posY, total, aces):

    '''process the specified card by drawing it in the window at posX
    and posY, update the total score and the number of aces; returns
    posX for next card, total and number of aces'''

    value, filename = cardInfo(card)
    # bonus for aces
    if value == 11:
        aces += 1
    total += value
    # bonus for aces
    total, aces = aceScore(total, aces)
    drawCard(filename, posX, posY, win)
    posX += 100
    return posX, total, aces

#----------------------------------------------------------------------

def getWinner(player, dealer):
    
    # if neither busted
    if player <= 21 and dealer <= 21:
        if player > dealer:
            msg = 'you win!'
        elif player < dealer:
            msg = 'dealer wins'
        else:
            msg = 'tie'
    elif player > 21:
        msg = 'dealer wins'
    else:
        msg = 'you win!'
    return msg

#----------------------------------------------------------------------

def main(argv):

    '''play a game of blackjack'''

    win = createWindow()

    # get deck of cards
    d = CardDeck()
    d.shuffle()

    # keep track of scores
    playerTotal = 0
    dealerTotal = 0

    # bonus - keep track of # of aces
    playerAces = 0
    dealerAces = 0

    # keep track of position to display next card for player
    playerPos = 100

    # deal first card to player
    c = d.dealOne()
    playerPos, playerTotal, playerAces = processCard(
        c, win, playerPos, 100, playerTotal, playerAces)

    # deal second card to player
    c = d.dealOne()
    playerPos, playerTotal, playerAces = processCard(
        c, win, playerPos, 100, playerTotal, playerAces)

    # display total for the player
    playerText = Text(Point(100, 200), '')
    playerText.draw(win)
    displayScore(playerText, playerTotal)

    # keep track of position to display next card for dealer
    dealerPos = 100

    # deal first card to dealer
    c = d.dealOne()
    dealerPos, dealerTotal, dealerAces = processCard(
        c, win, dealerPos, 300, dealerTotal, dealerAces)

    # display total for the dealer
    dealerText = Text(Point(100, 400), '')
    dealerText.draw(win)
    displayScore(dealerText, dealerTotal)

    # keep dealing cards to player while they keep clicking mouse
    # inside "hit me" button and don't bust
    while playerTotal <= 21:
        # get mouse click and its location
        press = win.getMouse()
        x, y = press.getX(), press.getY()

        # if click inside hit me button
        if x >= 650 and x <= 750 and y >= 100 and y <= 150:
            # deal a card to player
            c = d.dealOne()
            playerPos, playerTotal, playerAces = processCard(
                c, win, playerPos, 100, playerTotal, playerAces)

            # display score for player
            displayScore(playerText, playerTotal)
        else:
            # stop if they click outside hit me button
            break

    # if player didn't bust
    if playerTotal <= 21:
        # dealer gets cards until has at least 17
        while dealerTotal < 17:
            # deal card to dealer
            c = d.dealOne()
            dealerPos, dealerTotal, dealerAces = processCard(
                c, win, dealerPos, 300, dealerTotal, dealerAces)

            # display score for dealer
            displayScore(dealerText, dealerTotal)

    # determine winner
    msg = getWinner(playerTotal, dealerTotal)
    
    # show winner
    winner = Text(Point(100, 500), msg)
    winner.draw(win)

    # wait for mouse click before closing window
    win.getMouse()
    win.close()
    
#----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
