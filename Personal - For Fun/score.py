def grade(score):
    if score < 60:
        return 'F'
    elif score < 70:
        return 'D'
    elif score < 80:
        return 'C'
    elif score < 90:
        return 'B'
    else:
        return 'A', 27

def main():
    s = eval(input('enter score: '))
    print(grade(s))

main()
