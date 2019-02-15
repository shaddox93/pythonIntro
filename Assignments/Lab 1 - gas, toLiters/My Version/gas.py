#gas.py
#A program to determine money spent on gas annually
#CS160 1PM - Victor Stasek

def main():
    print("This program calculates money spent on gas annually.") 
    print()
    
    miles = eval(input("Enter number of miles driven per month: "))
    mpg = eval(input("Enter average miles per gallon for your car: "))
    gasPrice = eval(input("Enter price of gas per gallon in dollars: "))
    annualGas1 = (miles / mpg) * gasPrice * 12
    annualGas2 = (miles / mpg) * (gasPrice + 1) * 12
    print()

    print("Annual gas cost:", annualGas1)
    print("Annual gas cost if price goes up $1:", annualGas2)

main()
