def fib(n):
    if n < 2:
        return 1
    else:
        prev = 1
        curr = 1
        for i in range(n-1):
            temp = prev + curr
            prev = curr
            curr = temp
        return temp
def main():
    n = eval(input('Enter n: '))
    print(fib(n))

main()
