def dicks():
    dickSize = eval(input("How many inches is your dick?: "))
    if dickSize <= 8 and dickSize > 0:
        print("8", end="")
        for i in range(int(dickSize)):
            print("=", end="")
        print("D")
    elif dickSize <= 0:
        print("({})")
    else:
        print("Liar.")

while(True):
    dicks()
