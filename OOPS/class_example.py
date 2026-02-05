# created a class
class Car:
    make = 2020
    company = "Maruti"
    color = "White"

    def getInfo(self):
        print(f"Car is a {self.color} {self.company} made in {self.make}")


# created a object
baleno = Car()

# used property of class via object
print(f"Color is {baleno.color}") #White

# used method of class
print(baleno.getInfo())