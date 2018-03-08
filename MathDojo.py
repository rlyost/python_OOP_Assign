class MathDojo(object):
    def __init__(self):
        self.total = 0
        num1 = 0
        num2 = 0
    def add(self, *num1):
        for num1 in num1:
            if type(num1) == list:
                for i in num1:
                    self.total += i
            elif type(num1) == tuple:
                for i in num1:
                    self.total += i
            else:
                self.total += num1
        return self
    def subtract(self, *num2):
        for num2 in num2:
            if type(num2) == list:
                for i in num2:
                    self.total -= i
            elif type(num2) == tuple:
                for i in num2:
                    self.total -= i
            else:
                self.total -= num2
        return self
    def result(self):
        print self.total

md = MathDojo()
# md.add(2).add(2,5).subtract(3,2).result()

# md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
md.add(45).subtract([1.1, 2.3, 0],(2, 3, 4)).result()