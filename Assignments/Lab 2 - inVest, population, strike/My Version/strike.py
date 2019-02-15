#strike.py
#A program that estimates the distance in miles to a lightning strike
#CS160 1PM - Victor Stasek

def main():
    print("This program calculates the distance in miles to a lightning strike.")
    print()
    
    seconds = eval(input("Enter time between lightning flash and thunder in seconds: "))
    #sound travels 1,100 feet per second and 1 mile is 5,280 feet
    miles = seconds * (1100/5280)

    print("The lightning was", miles, "miles away.")

main()
