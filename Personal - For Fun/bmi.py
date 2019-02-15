def main():
    w = eval(input('Enter weight in pounds: '))
    h = eval(input('Enter height in inches: '))
    bmi = (w * 720) / (h * h)
    if bmi >= 19 and bmi <= 25:
        print("healthy")
    else:
        print("unhealthy")
main()
