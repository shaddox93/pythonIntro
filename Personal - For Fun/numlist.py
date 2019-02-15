def sumList(nums):
    nums = nums.split()
    eval(nums)
    y = 0
    for i in range(nums):
        eval(i)
        y = y + i
    return i
    
def main():
    x = input("Enter a list of numbers: ")
    haha = sumList(x)
    print(haha)

main()
    
