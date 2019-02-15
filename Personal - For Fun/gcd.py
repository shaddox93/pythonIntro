def main():
    n, m = eval(input('enter two numbers seperated : '))
    while m != 0:
        n, m = m, n%m
    print(n)
        
main()
