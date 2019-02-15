def main():

    s = input('enter numbers seperated by a comma: ')
    items = s.split(',')
    for i in range(len(items)):
        items[i] = eval(items[i])

    max = 0
    for x in items:
        if x > max:
            max = x
    print(max)

main()
