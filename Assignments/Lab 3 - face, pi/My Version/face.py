# face.py
# A program that illustrates a face in a graphics window
# CS160 1PM - Victor Stasek

from graphics import *

def main():
    # Open a graphing window
    win = GraphWin('Face', 400, 400)
    win.setBackground('orange')

    # Draw face
    center = win.getMouse()
    face = Circle(center, 100)

    face.setFill('cyan')
    face.draw(win)
    center.draw(win)

    # Draw eyes
    leftEye = Circle(center, 10)
    leftEye.move(-25, -15)
    
    rightEye = Circle(center, 10)
    rightEye.move(25, -15)

    leftEye.setFill('red3')
    leftEye.draw(win)
    rightEye.setFill('red')
    rightEye.draw(win)

    # Draw mouth
    mouth = Oval(Point(center.getX() - 25, center.getY() - 15), Point(center.getX() + 25, center.getY() + 15))
    mouth.move(0, 40)
    
    mouth.setFill('red2')
    mouth.draw(win)

    # Draw beard
    beard1 = Oval(Point(center.getX() - 50, center.getY() - 30), Point(center.getX() + 50, center.getY() + 30))
    beard1.move(0, 100)

    beard2 = Oval(Point(center.getX() - 40, center.getY() - 25), Point(center.getX() + 40, center.getY() + 25))
    beard2.move(0, 140)

    beard3 = Oval(Point(center.getX() - 32.5, center.getY() - 22.5), Point(center.getX() + 32.5, center.getY() + 22.5))
    beard3.move(0, 165)
    
    beard1.setFill('black')
    beard1.draw(win)
    beard2.setFill('black')
    beard2.draw(win)
    beard3.setFill('black')
    beard3.draw(win)

    # Draw headband
    headBand = Rectangle(Point(center.getX() - 95, center.getY() - 15), Point(center.getX() + 95, center.getY() + 15))
    headBand.move(0, -50)

    headBand.setFill('purple')
    headBand.draw(win)

    # Draw text
    words = Text(Point(center.getX(), center.getY() - 120), "Ninja Squirtle")

    words.setTextColor('cyan')
    words.draw(win)
    
    # Wait for mouse click to close window
    win.getMouse()
    win.close()
    
main()
