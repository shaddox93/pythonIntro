def main():
    x1, x2 = eval(input("Enter two numbers seperated by a comma: "))
    outfile = open("dicks.doc", "w")
    s = x1 + x2
    d = x1 - x2
    print("The sum is", s, "and the difference is", d, file=outfile)
    outfile.close()

main()
