# population.py
# a program that estimates a future population
# CS160 1PM - Victor Stasek

def main():
    print("This program estimates a future population of the U.S.")
    print()

    # get input from user for calculations
    years = eval(input("Enter number of years: "))

    # calculate annual population increase
    # someone is born every 8 secs, dies every 14 secs, and immigrates into the US every 46 seconds
    # (60/8) - (60/14) + (60/46) = the population increase per minute = 4.5186
    # 4.5186 * 60 * 24 * 365.25 = population increase per year = 2376620.496
    
    # multiply annual population increase by number of years, then add current population
    populationInFuture = years * 2376620.49 + 314254374
    print("The estimated population in", years, "years is", int(populationInFuture))

main()
