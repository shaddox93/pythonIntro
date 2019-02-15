
from graphics import *

def main():
    #Open graphing window
    win = GraphWin('House')

    #Draw house frame
    p1 = win.getMouse()
    p2 = win.getMouse()
    frame = Rectangle(p1, p2)
    p1.draw(win)
    p2.draw(win)
    frame.draw(win)

    #Draw door
    p3 = win.getMouse()
    doorWidth = 1/5*(p2.getX() - p1.getX())
    p4 = Point(p3.getX() + 1/2*(doorWidth), p3.getY())    
    p5 = Point(p3.getX() - 1/2*doorWidth, p1.getY())
    door = Rectangle(p4, p5)
    door.draw(win)

    #Draw window
    p6 = win.getMouse()
    
    
    
main()
