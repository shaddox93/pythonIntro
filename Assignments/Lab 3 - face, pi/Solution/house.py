#!/usr/bin/env python
# Dave Reed
# CS160

#-----------------------------------------------------------------------

from graphics import *

#-----------------------------------------------------------------------

def main():

    '''draws a house as specified by 5 mouse clicks and proportions
    specified in comments'''
    
    win = GraphWin('Draw a House', 400, 400)

    # first two clicks define base of house
    bottomLeft = win.getMouse()
    topRight = win.getMouse()

    base = Rectangle(bottomLeft, topRight)
    base.draw(win)

    # door width is 1/5 of base with top center at 3rd mouse click
    doorWidth = 0.2 * (topRight.getX() - bottomLeft.getX())
    doorCenter = win.getMouse()

    doorBottomX = doorCenter.getX() - 0.5 * doorWidth
    doorBottomLeft = Point(doorBottomX, bottomLeft.getY())
    
    doorTopX = doorCenter.getX() + 0.5 * doorWidth
    doorTopRight = Point(doorTopX, doorCenter.getY())

    door = Rectangle(doorBottomLeft, doorTopRight)
    door.draw(win)

    # square window is centered at 4th mouse click with 1/2 width of door
    windowCenter = win.getMouse()
    windowHalfWidth = 0.25 * doorWidth
    windowBottomX = windowCenter.getX() - windowHalfWidth
    windowBottomY = windowCenter.getY() - windowHalfWidth
    windowBottomLeft = Point(windowBottomX, windowBottomY)
    
    windowTopX = windowCenter.getX() + windowHalfWidth
    windowTopY = windowCenter.getY() + windowHalfWidth
    windowTopRight = Point(windowTopX, windowTopY)
    
    window = Rectangle(windowBottomLeft, windowTopRight)
    window.draw(win)

    # peak top is at 5th mouse click
    peak = win.getMouse()
    topLeft = Point(bottomLeft.getX(), topRight.getY())
    peak = Polygon(topLeft, peak, topRight)
    peak.draw(win)
    
    win.getMouse()
    win.close()
    
#-----------------------------------------------------------------------

main()
