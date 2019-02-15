#!/usr/bin/env python

#----------------------------------------------------------------------
# face.py
# Dave Reed
# 09/17/2012
#----------------------------------------------------------------------

from graphics import *

#----------------------------------------------------------------------

#----------------------------------------------------------------------

def main():

    # create window
    win = GraphWin("Face", 400, 400)

    # get click for center of face
    center = win.getMouse()
    circle = Circle(center, 100)
    circle.draw(win)

    # left eye center is 25 pixels above and 15 pixels to the left
    # of the face center
    leftPt = Point(center.getX() - 25, center.getY() - 15)
    # right eye center is 25 pixels above and 15 pixels to the right
    # of the face center
    rightPt = Point(center.getX() + 25, center.getY() - 15)

    # draw eyes with radius 10
    leftEye = Circle(leftPt, 10)
    leftEye.draw(win)
    rightEye = Circle(rightPt, 10)
    rightEye.draw(win)

    # mouth center is 40 pixels below the face center
    mouthCenter = Point(center.getX(), center.getY() + 40)
    # make points for lower left and upper right points of mouth oval
    left = mouthCenter.clone()
    right = mouthCenter.clone()

    # oval is 50 pxiels wide and 30 pixels high
    left.move(-25, 15)
    right.move(25, -15)

    # create and draw mout
    oval = Oval(left, right)
    oval.draw(win)

    # wait for mouse click and then close window
    win.getMouse()
    win.close()
    
#----------------------------------------------------------------------

main()

