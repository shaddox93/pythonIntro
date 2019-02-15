# File: chaos.py
# A simple program comparing chaotic behavior between two numbers.

def main():
    print('This program illustrates a chaotic function')
    print('')
    x = eval(input('Enter a number between 0 and 1 for x: '))
    print('')
    print('x')
    print('-----------')
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)
    print('')
    y = eval(input('Enter a number between 0 and 1 for y: '))
    print('')
    print('y')
    print('----------')
    for i in range(10):
        y = 3.9 * y * (1 - y)
        print(y)
    
main()
