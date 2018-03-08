class Products(object):
    def __init__(self, price, item, weight, brand, status):
        self.price = price
        self.item = item
        self.weight = weight
        self.brand = brand
        self.status = status
    def sell(self):
        self.status = "sold"
    def addTax(self,rate):
        self.price = self.price * (rate + 1)
    def Return(self,reason,box):
        if reason == "defective":
            self.status = reason
            self.price = 0
        elif box == "opened":
            self.status = "used"
            self.price = self.price * .8
        else:
            self.status = "for sale"
    def display_info(self):
        print "Price: " + str(self.price)
        print "Item: " + str(self.item)
        print "Weight: " + str(self.weight)
        print "Brand: " + str(self.brand)
        print "Status: " + str(self.status)

product1 = Products(12.34,"Sheep Shears",0.8,"Guber Industrial","for sale")
product1.Return("Did not like","not opened")
product1.display_info()