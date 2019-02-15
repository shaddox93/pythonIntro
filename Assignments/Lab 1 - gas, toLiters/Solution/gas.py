#!/usr/bin/env python

#----------------------------------------------------------------------
# gas.py
# Dave Reed
# 08/04/2011
#----------------------------------------------------------------------

def main():

    # get input for calculations
    miles = eval(input('Enter number of miles driven per month: '))
    mpg = eval(input('Enter average miles per gallon for your car: '))
    gasPrice = eval(input('Enter price of gas per gallon in dollars: '))

    # calculate annual cost for gas
    yearlyCost = miles * 12 / mpg * gasPrice
    print('Annual gas cost:', yearlyCost)

    # calculate annual cost for gas if gallon is $1 more expensive 
    yearlyCost = miles * 12 / mpg * (gasPrice + 1.0)
    print('Annual gas cost if price goes up $1:', yearlyCost)
    
#----------------------------------------------------------------------

main()
