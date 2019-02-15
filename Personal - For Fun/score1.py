def main():
    dicks = open('score.txt', 'w')
    score = eval(input("Enter score :"))
    grade = 'FFDCBA'
    grade = grade[score]
    print(grade, file=dicks)
    dicks.close()
main()
