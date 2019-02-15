#!/usr/bin/env python3

#----------------------------------------------------------------------
# acronym.py
# Dave Reed
# 10/03/2012
#----------------------------------------------------------------------

import sys

#----------------------------------------------------------------------

def acronym(phrase):

    result = []
    words = phrase.split()
    for w in words:
        result.append(w[0])
    result = ''.join(result)
    return result.upper()
    
#----------------------------------------------------------------------

def main(argv):
    s = input('enter phrase: ')
    print(acronym(s))

#----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
