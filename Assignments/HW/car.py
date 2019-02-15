class Car:
    
    def __init__(self, manufacturer, model, gts, mpg):
        
        self.manufacturer = manufacturer
        self.model = model
        self.gts = gts
        self.mpg = mpg

    def costToFillTank(self, costOfGas):
        
        return self.gts * costOfGass
    
    def maxDistance(self):
        
        return self.gts * self.mpg

    def carInfo(self):
        
        return self.manufacturer + ' ' + self.model
    
#----------------------------------------------------------------------

def main():
    
    auto1 = Car('Ford', 'Focus', 17, 35)
    print(auto1.carInfo())
    
main()
