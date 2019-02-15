#!/usr/bin/env python

#----------------------------------------------------------------------
# pi.py
# Dave Reed
# 09/17/2011
#----------------------------------------------------------------------

import math

#----------------------------------------------------------------------

def main():

    n = eval(input('enter number of terms to use to approximate pi: '))

    # accumulator variable and initial values for the term
    total = 0.0
    num = 4.0
    den = 1.0
    
    # loop to add terms
    # add terms 4/1 - 4/3 + 4/5 - 4/7 + 4/9 + ...
    for i in range(n):
        # add next term
        total = total + num / den
        # update num and den for next term
        num = num * -1.0
        den = den + 2.0

        # another version
        #total = total + (-1) ** i * 4.0 / (2 * i + 1)
                

    # output results
    print('the approximation is: ', total)
    print('the difference is: ', abs(total - math.pi))


#----------------------------------------------------------------------

main()

