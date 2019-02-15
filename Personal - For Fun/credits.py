def main():
    cred = eval(input("enter credits: "))
    if cred >= 0 and cred < 8:
        print("Freshman")
    elif cred >= 8 and cred < 17:
        print("Sophomore")
    elif cred >= 17 and cred < 27:
        print("Junior")
    else:
        print("Senior")
main()
