class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 15
        else:
            self.tax = 12
        self.display_all()
    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed)
        print "Fuel: " + self.fuel
        print "Mileage: " + str(self.mileage)
        print "Tax: " + str(self.tax)

    

Car1 = Car(2000,35,"Full",15)
Car2 = Car(2000,5,"Not Full",105)
Car3 = Car(2000,15,"King of Full",95)
Car4 = Car(2000,25,"Full",25)
Car5 = Car(2000,45,"Empty",25)
Car6 = Car(20000000,35,"Empty",15)
