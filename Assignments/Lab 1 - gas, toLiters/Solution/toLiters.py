#!/usr/bin/env python3

#----------------------------------------------------------------------
# toLiters.py
# Dave Reed
# CS160
# 08/14/2012
#----------------------------------------------------------------------

#----------------------------------------------------------------------

def main():
    quarts = eval(input('enter amount in quarts: '))
    # one gallon is 3.78541 liters and there are 4 quarts in a gallon
    liters = quarts / 4.0 * 3.78541
    print(quarts, 'quarts is', liters, 'liters')
    
#----------------------------------------------------------------------

main()

