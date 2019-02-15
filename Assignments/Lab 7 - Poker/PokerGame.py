#----------------------------------------------------------------------
# PokerGame.py
# Victor Stasek
# 11/28/2012
#----------------------------------------------------------------------

from CardDeck import *
from PokerHand import *
from Button import *
from graphics import *

#----------------------------------------------------------------------
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
    
    win = GraphWin('Poker', 800, 600)
    win.setBackground('green4')
    Text(Point(100, 40), 'Player 1').draw(win)
    Text(Point(100, 340), 'Player 2').draw(win)
    quitButton = Button(win, Point(725, 550), 80, 40, 'Quit')
    quitButton.activate()

    return win, quitButton

#----------------------------------------------------------------------
    
def drawFiveCards(d, player, startx, y, win):
    
    for i in range(5):
        c = d.dealOne()
        player.addCard(c)
        value, filename = cardInfo(c)
        drawCard(filename, startx, y, win)
        startx += 100  

#----------------------------------------------------------------------

def getWinner(value1, value2):

    if value1 > value2:
        msg = 'Player 1 Wins!'
    elif value2 > value1:
        msg = 'Player 2 Wins!'
    else:
        msg = ''

    return msg

#----------------------------------------------------------------------
    
def drawHandType(y, player, win):

    handValue = player.evalHand()
    Text(Point(300, y), PokerHand.HAND_NAMES[handValue]).draw(win)

    return handValue

#----------------------------------------------------------------------
    
def main():

    win, quitButton = createWindow()
    
    d = CardDeck()
    d.shuffle()

    player1 = PokerHand()
    player2 = PokerHand()    
    
    drawFiveCards(d, player1, 100, 100, win)
    drawFiveCards(d, player2, 100, 400, win)
    
    handValue1 = drawHandType(200, player1, win)
    handValue2 = drawHandType(500, player2, win)

    msg = getWinner(handValue1, handValue2)
    Text(Point(600, 550), msg).draw(win)

    x = win.getMouse()
    while not quitButton.clicked(x):
        x = win.getMouse()
        
    win.close()
    
main()
