#!/usr/bin/env python3

#----------------------------------------------------------------------
# distance.py
# Dave Reed
# 08/28/2012
#----------------------------------------------------------------------

def main():

    time = eval(input('Enter time between lightning flash and thunder: '))
    # sounds travels 1100 ft/sec and 1 mile is 5280 ft.
    dist = time * 1100 / 5280.0
    print('The lightning was', dist, 'miles away.')

#----------------------------------------------------------------------

main()
