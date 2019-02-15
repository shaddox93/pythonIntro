# File: chaos.py
# A simple program comparing chaotic behavior between two numbers.

def main():
    print('This program illustrates a chaotic function')
    
    x = eval(input('Enter a number between 0 and 1 for x: '))
    y = eval(input('Enter a number between 0 and 1 for y: '))
    print()
    print('x =', x, '| y =', y)
    print('---------------------------------------')
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print(round(x, 3),'|', round(y, 3))

main()
