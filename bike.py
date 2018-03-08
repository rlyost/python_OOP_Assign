class bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print "Price: " + str(self.price)
        print "Max speed: " + str(self.max_speed)
        print "Miles: " + str(self.miles)
    def ride(self):
        print "Riding!"
        self.miles += 10
    def reverse(self):
        print "Reversing!"
        self.miles -= 5
        
bike1 = bike(100,30,580)
bike2 = bike(150,38,210)
bike3 = bike(750,88,15)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()



