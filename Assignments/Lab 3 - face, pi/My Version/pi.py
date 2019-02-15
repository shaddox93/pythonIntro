# pi.py
# a program that estimates the value of pi
# CS160 1PM - Victor Stasek

import math

def main():

    # Get number of terms to use from user
    terms = eval(input("Enter number of terms to use to approximate pi: "))

    # Approximate pi
    x = 1
    z = 0
    for i in range(1, terms + 1):
        approxPi = z + (4/x)
        x = x + 2
        z = approxPi * -1
    print("The approximation is: ", abs(approxPi))
    
    # Find difference between approximation and pi
    print("The difference is: ", abs(approxPi - math.pi))# math.pi - abs(approxPi))

main()
