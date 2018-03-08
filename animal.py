class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health = self.health - 1
        return self
    def run(self):
        self.health = self.health - 5
        return self
    def display_health(self):
        print self.name,self.health
        return self
Animal1 = Animal("Wolf",98)
Animal1.walk().walk().walk()
Animal1.run().run()
Animal1.display_health()
class Dog(Animal):
    def set_health(self):
        self.health = 150
        return self
    def pet(self):
        self.health = self.health + 5
        return self
d1 = Dog("Lab",95)
d1.set_health()
d1.walk().walk().walk().run().run()
d1.pet()
d1.display_health()
class Dragon(Animal):
    def set_health(self):
        self.health = 170
        return self
    def fly(self):
        set_health = set_health - 10
        return self
    def dragon_health(self):
        print "I am a Dragon"
        self.display_health()
        return self
dragon1 = Dragon("Fire",87)
dragon1.set_health()
Animal1.display_health()
dragon1.dragon_health()