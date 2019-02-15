#----------------------------------------------------------------------
# blackjack.py
# Victor Stasek
# 11/13/2011
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

    '''returns the blackjack value, filename for card specified
    by cardNumber, and whether or not an ace is drawn

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

    # calculate suit and face numbers
    suitNum = cardNumber // 13
    faceNum = cardNumber % 13

    # calculate blackjack value
    aces = 0
    value = faceNum + 1
    if value > 10:
        value = 10
    elif value == 1:
        value = 11
    # if an ace is drawn, adds one to ace counter
        aces += 1

    # calculate name of file
    # face is a number from 1 to 13 with leading zeros for 1-9
    suits = 'cshd'
    filename = '{:>02}{}.gif'.format(faceNum + 1, suits[suitNum])
    return value, filename, aces

#----------------------------------------------------------------------

def button(win):

    '''draws a rectangle which serves as the 'hit me' button.'''
      
    # draws a rectangle in win, sets its color to gray
    button = Rectangle(Point(650, 125), Point(750, 175))
    button.setFill('lightgray')
    button.draw(win)
    # draws text in the middle of the rectangle
    Text(Point(700, 150), "Hit Me!").draw(win)

#----------------------------------------------------------------------

def player(deck, startx, y, win):

    '''deals the player's inital two cards from the CardDeck deck and
    displays them in the GraphWin win in the row specified by the int
    y starting at the x coordinate specified by the int startx and moves
    over 100 pixels for each new card; returns the blackjack total for
    the initial two cards and the # of aces the player received'''

    total = 0
    playerAces = 0
    for i in range(2):
        # deal a card and draw it in win
        card = deck.dealOne()
        value, filename, aces = cardInfo(card)
        drawCard(filename, startx, y, win)
        # move x over 100 pixels for next card
        startx += 100
        # accumulate player's total for all the cards
        total += value
        # records how many aces the player has
        playerAces += aces
        
    return total, playerAces
    
#----------------------------------------------------------------------

def dealer(deck, win):

    '''deals the dealer's initial card from the CardDeck deck and
    displays it in the GraphWin win at y = 325; returns the value
    of the dealer's card and the # of aces the dealer received.'''
    
    # deal a card and draw it in win
    card = deck.dealOne()
    value, filename, aces = cardInfo(card)
    drawCard(filename, 100, 325, win)

    return value, aces

#----------------------------------------------------------------------

def hitMe(deck, x, y, win):

    '''deals a card from the CardDeck deck and displays it in the
    GraphWin win in the row specified by the int y and the x coordinate
    specified by the int x; returns value of the card drawn and the #
    of aces received'''

    # deal a card and draw it in win
    card = deck.dealOne()
    value, filename, aces = cardInfo(card)
    drawCard(filename, x, y, win)
    
    return value, aces
#----------------------------------------------------------------------

def main():

    # create a graph window
    win = GraphWin('Blackjack', 800, 600)
    # set window background to green
    win.setBackground('green4')
    
    # create card deck and shuffle it
    deck = CardDeck()
    deck.shuffle()

    # call the player function and assign player's total value to
    # playerTotal and number of aces drawn to playerAces
    playerTotal, playerAces = player(deck, 100, 100, win)

    # handles rare case in which player receives two aces on first draw
    if playerTotal == 22 and playerAces == 2:
        playerTotal, playerAces = 12, 1
    
    # displays player's total value in win and assigns it to playerMsg
    playerMsg = Text(Point(100, 175), "Total: {}".format(playerTotal))
    playerMsg.draw(win)

    # calls the dealer function and assigns dealer's total value to
    # dealerTotal and number of aces drawn to dealerAces
    dealerTotal, dealerAces = dealer(deck, win)
    # displays dealer's total value in win and assigns it to dealerMsg
    dealerMsg = Text(Point(100, 400), "Total: {}".format(dealerTotal))
    dealerMsg.draw(win)

    # draws the button used for 'hit me'
    button(win)

    # this section deals with drawing the player's cards after the initial
    # two cards are drawn
    
    # automatically deals for the dealer if the player's initial two cards
    # put playerTotal at 21
    if playerTotal == 21:
        pass
    else:
        startx = 300
        # wait for a mouse click to see if player wants to hit or stay
        x = win.getMouse()
        # if player clicks button, loop begins; loops ends when player clicks
        # outside of the button (decides to stay) or player's total is over 21
        while (playerTotal < 21 and x.getX() >= 650
              and x.getX() <= 750 and x.getY() >= 125 and x.getY() <= 175):
            # assign value of the card drawn to value and the number of
            # aces drawn to aces
            value, aces = hitMe(deck, startx, 100, win)
            # move startx over for next card
            startx += 100
            # add value of card to playerTotal
            playerTotal += value
            # add 1 to playerAces if an ace was drawn
            playerAces += aces
            # update player's total in win
            playerMsg.setText("Total: {}".format(playerTotal))

            # if player hasn't busted, wait for a mouse click to see if they
            # want to hit or stay; if player stays, loop terminates
            if playerTotal < 21:
                x = win.getMouse()

            # if player busts but has an ace:
            elif playerTotal > 21 and playerAces > 0:
                # subtract ten from playerTotal to simulate an ace changing
                # from 11 to 1
                playerTotal -= 10
                # subtract 1 from player's total aces
                playerAces -= 1
                # update playerTotal displayed in win
                playerMsg.setText("Total: {}".format(playerTotal))
                # wait for a click to see if player wants to hit or stay
                x = win.getMouse()
                
            # if player busts and has no aces
            elif playerTotal > 21 and playerAces == 0:
                Text(Point(100, 500), "Dealer Wins!").draw(win)
                Text(Point(100, 200), "Player Busted").draw(win)

    # this section deals with drawing the dealer's cards
    # if playerTotal is over 21, the daler has already won
    if playerTotal > 21:
        pass
    else:
        startx = 200
        # loop terminates when dealerTotal is greater than 17
        while dealerTotal < 17:
            # assign value of card drawn to value and number of aces
            #drawn to aces
            value, aces = hitMe(deck, startx, 325, win)
            # move startx over 100 pixels for next card
            startx += 100
            # add value of card to dealerTotal
            dealerTotal += value
            # add 1 to dealerAces if an ace was drawn
            dealerAces += aces
            # update dealer's total in win
            dealerMsg.setText("Total: {}".format(dealerTotal))

            # if dealer busts but has an ace:
            if dealerTotal > 21 and dealerAces > 0:
                # subtract 10 from dealer's total score to simulate
                # ace changing from 11 to 1
                dealerTotal -= 10
                # subtract 1 from dealer's total aces
                dealerAces -= 1
                # update dalerTotal displayed in win
                dealerMsg.setText("Total: {}".format(dealerTotal))
            
    # find out who won
    # if dealer busts player wins
    if dealerTotal > 21:
        Text(Point(100, 500), "Player Wins!").draw(win)
        Text(Point(100, 425), "Dealer Busted").draw(win)
    # if player's total is higher than dealer's total and player hasn't busted
    # player wins
    elif playerTotal > dealerTotal and playerTotal <= 21:
        Text(Point(100, 500), "Player Wins!").draw(win)
    # if dealer's total is higher than player's total, dealer wins
    elif dealerTotal > playerTotal:
        Text(Point(100, 500), "Dealer Wins!").draw(win)
    # if player's total and dealer's total are the same, tie
    elif playerTotal == dealerTotal:
        Text(Point(100, 500), "Tie").draw(win)
        
    # wait for mouse click before closing window
    win.getMouse()
    win.close()
    
#----------------------------------------------------------------------

if __name__ == '__main__':
    main()
