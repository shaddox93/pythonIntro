def main():
    
    hours = eval(input("How many hours per week do you work?: "))
    wage = eval(input("What is your hourly wage?: "))

    if hours > 40:
        grossWage = (40*wage)+(hours-40)*(wage*1.5)
        print("You earned ${:0.2f}".format(grossWage))
    else:
        grossWage = hours*wage
        print("You earned ${:0.2f}".format(grossWage))
main()
