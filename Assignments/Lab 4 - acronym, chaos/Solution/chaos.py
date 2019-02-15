#!/usr/bin/env python3

#----------------------------------------------------------------------
# chaos.py
# Dave Reed
# 10/03/2012
#----------------------------------------------------------------------

def main():
	
    x1, x2 = eval(input('enter x1 and x2 separated by a comma: '))
    # open output.txt file for writing
    outfile = open('output.txt', 'w')
    # print header line to file
    print('index{:8.2f}{:13.2f}'.format(x1, x2), file=outfile)
    # print separator line to file
    print(28 * '-', file=outfile)
    for i in range(10):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        # print updated values to file
        print('{:3}{:12.6f} {:12.6f}'.format(i+1, x1, x2), file=outfile)
    outfile.close()
	
#----------------------------------------------------------------------

if __name__ == '__main__':
    main()
