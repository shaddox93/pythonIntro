class Statistics:

    def __init__(self, seq=None):

        self.items = []
        if seq != None:
            for x in seq:
                self.items.append(x)
        
    def inputNumbers(self):
        
        xStr = input('enter a number: ')
        while xStr != '':
            x = eval(xStr)
            self.items.append(x)
            xStr = input('enter a number: ')
        

    def mean(self):

        total = 0.0
        for x in self.items:
            total += x
        return total / len(self.items)

    def median(self):

        values = self.items[:]
        values.sort()
        middle = len(values) // 2
        if len(values) % 2 == 0:
            return (values[middle] + values[middle-1]) / 2.0
        else:
            return values[middle]

    def addNumber(self, x):

        self.items.append(x)

    def printList(self):

        print(self.items)

def main():

    s = Statistics([2, 3, 4])
    s.inputNumbers()
    s.addNumber(7)
    mean = s.mean()
    median = s.median()
    print('mean = {:10.2f} median = {:10.2f}'.format(mean, median))

if __name__ == '__main__':
    main()
    
