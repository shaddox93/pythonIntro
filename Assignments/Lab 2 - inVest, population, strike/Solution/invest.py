#!/usr/bin/env python3

#----------------------------------------------------------------------
# invest.py
# Dave Reed
# 08/28/2012
#----------------------------------------------------------------------

def main():

    amount = float(input('Enter annual amount invested in IRA: '))
    interest_rate = float(input('Enter interest rate (e.g., 0.05 for 5%): '))
    years = int(input('Enter number of years: '))

    value = 0
    print('year, value')
    for i in range(years):
        # add annual amount to current total and then apply interest
        value = (value + amount) * (1 + interest_rate)
        print(i+1, ',', round(value, 2))

#----------------------------------------------------------------------

main()
