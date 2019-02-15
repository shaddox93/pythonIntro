# Temperature Converter.py
# A program to convert Celcius temps to Fahrenheit

def main():
    for celsius in range(0, 101, 10):
        #celsius = i * 10
        fahrenheit = 9/5 * celsius + 32
        print(celsius, fahrenheit)

main()
