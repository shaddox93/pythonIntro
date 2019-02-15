def main():
    minutes = eval(input("Enter a number of minutes: "))
    print("{0}:{1:0>2}".format(minutes//60, minutes%60))
main()
