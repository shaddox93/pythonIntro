# invest.py
# a program to calculate money earned from annual interest with a fixed annual principle
# CS160 1PM - Victor Stasek

def main():
    
    print("This program calculates money earned")
    print("from annual interest with a fixed annual principle.")
    print()

    # get input from user for calculations
    principal = eval(input("Enter annual amount invested in IRA: "))
    apr = eval(input("Enter interest rate (e.g., 0.05 for 5%): "))
    years = eval(input("Enter number of years for the investment: "))
    print()

    
    print("year | value")
    base = 0
    # each loop adds yearly principal to base (current amount), then mult. by interest rate
    for i in range(1, years + 1):
        base = (base + principal) * (1 + apr)
        print(i, '|',  base)

main()
