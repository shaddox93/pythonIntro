# chaos.py
# a program that illustrates chaos theory
# CS160-1PM - Victor Stasek

# chaos(var) function performs the chaos expression on a number and returns the output
def chaos(var):
    var = 3.9 * var * (1 - var)
    return var

def main():
    # Open a file to save the output to called output.txt
    chaosFile = open('output.txt', 'w')

    # Get two numbers from user
    x1, x2 = eval(input("Enter x1 and x2 seperated by a comma: "))

    # Print header to file
    print("index{:8.2f}{:13.2f}".format(x1, x2), file=chaosFile)
    print("-" * 28, file=chaosFile)

    # Loop through chaos function ten times for each variable and prints the output
    for i in range(1, 11):
        x1 = chaos(x1)
        x2 = chaos(x2)
        print("{:3}{:12.6f}{:13.6f}".format(i, x1, x2), file=chaosFile)

    # Close the file output.txt
    chaosFile.close()
    
main()
