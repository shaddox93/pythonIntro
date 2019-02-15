# File: chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print('This program illustrates a chaotic function')
    x = eval(input('enter a number between 0 and 1: '))
    print()
    for i in range(398374953979753439938398745789378943978):
        x = 3.9 * x * (1 - x)
        print(x)

main()
