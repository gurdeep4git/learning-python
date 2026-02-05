# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
    
#     def getAge(self):
#         return self.__age    
    
#     def setAge(self, age):
#         self.__age = age

# p = Person("John", 21)
# p.setAge(35)
# print(p.getAge())

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
    @property
    def age(self):
        return self.__age    #getter
    
    @age.setter
    def age(self, age):
        self.__age = age     #setter

p = Person("John", 21)
p.age = 35
print(p.age)