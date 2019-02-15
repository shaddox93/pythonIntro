#!/usr/bin/env python

#----------------------------------------------------------------------
# ExampleClasses.py
# Dave Reed
# 11/06/2012
#----------------------------------------------------------------------

import sys

#----------------------------------------------------------------------

class Point:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def getX(self):
        
        return self.x

    def getY(self):
        
        return self.y

    def move(self, dx, dy):

        self.x += dx
        self.y += dy

#----------------------------------------------------------------------

class Rectangle:

    def __init__(self, centerPoint, w, h):

        self.centerPoint = centerPoint
        self.width = w
        self.height = h

    # do not name instance variables and methods the same or it will not work
    # so I use getCenterPoint rather than the method centerPoint
    def getCenterPoint(self):

        return self.centerPoint
    
    def area(self):

        return self.width * self.height

    def move(self, dx, dy):

        self.centerPoint.move(dx, dy)

    def getLowerLeftPoint(self):

        halfWidth = self.width / 2
        halfHeight = self.height / 2
        p = Point(self.centerPoint.getX() - halfWidth,
                  self.centerPoint.getY() + halfHeight)
        return p

#----------------------------------------------------------------------

def main(argv):

    p = Point(10, 20)
    print(p.getX(), p.getY())

    r = Rectangle(p, 100, 200)
    r.move(10, 5)
    lowerLeft = r.getLowerLeftPoint()
    print(lowerLeft.getX(), lowerLeft.getY())

    center = r.getCenterPoint()
    print(center.getX(), center.getY())

    # why isn't this 10, 20?
    print(p.getX(), p.getY())
    

#----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
