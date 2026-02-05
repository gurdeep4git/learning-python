class Car:
    def __init__(self, name, make):
        self.name = name
        self.make = make

    def move(self):
        print(f"{self.name} drives")    


class Plane:
    def __init__(self, name, make):
        self.name = name
        self.make = make

    def move(self):
        print(f"{self.name} flies")


car = Car("Baleno", 2020)
plane = Plane("Boeing A60", 2025)

for x in [car, plane]:
    x.move() # different objects can respond to the same method or operation in their own way.





