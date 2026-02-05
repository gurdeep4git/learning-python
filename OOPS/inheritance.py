class Person:
    def __init__(self, name, age):
        self.name =  name
        self.age = age

    def printInfo(self):    
        print(f"{self.name} is {self.age} years old")


class Student(Person):
    def __init__(self, name, age, gradYear):
        super().__init__(name, age)
        self.gradYear = gradYear

    def printStudentInfo(self):
        print(f"Students is {self.name}, {self.age} years of age, studying in class of year {self.gradYear}")    

student = Student("John", 25, 2022)
student.printStudentInfo()