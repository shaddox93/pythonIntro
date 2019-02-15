#toLiters.py
#A program that converts quarts to liters
#CS160 1PM - Victor Stasek

def main():
    print("This program converts quarts to liters.")
    print()

    quarts = eval(input("Enter the amount in quarts: "))
    liters = quarts * 0.9463525
                  
    print(quarts, "quarts is", liters, "liters.")

main()
