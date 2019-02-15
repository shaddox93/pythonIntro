#Victor Stasek

from graphics import *

def main():
    #Open a graphing window
    win = GraphWin('Rectangle')
    
    #Draw a rectangle
    p1 = win.getMouse()
    p2 = win.getMouse()
    rect = Rectangle(p1, p2)
    rect.draw(win)

    #Find the area of the rectangle
    area = abs((p1.getX() - p2.getX()) * (p1.getY() - p2.getY()))

    #Find the center of the rectangle
    p3 = rect.getCenter()

    #Draw text
    areaLabel = Text(p3, area)
    areaLabel.draw(win)

    #Wait for mouse click to close program
    win.getMouse()
    win.close()
    
main()
