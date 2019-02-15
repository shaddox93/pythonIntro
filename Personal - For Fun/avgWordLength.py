def main():
    phrase = input('enter phrase: ')
    phraseLength = len(phrase.split())

    y = 0
    for ch in phrase.split():
        x = len(ch)
        y = y + x
    avgLength = y / phraseLength
    print(avgLength)
main()
