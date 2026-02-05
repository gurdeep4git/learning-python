class Car:
    #constructor
    def __init__(self, color, company, make):
        self.color = color     #object properties
        self.company = company #object properties
        self.make = make       #object properties

    def getColor(self):
        return f"Color is {self.color}"
    
    def addSpeakers(self, speakerBrand):
        print(f"{speakerBrand} Speakers added")
    
baleno = Car("white", "Maruti", 2020);    
baleno.addSpeakers("HARMAN")

        