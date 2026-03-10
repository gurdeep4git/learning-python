class Student():
    average = 0
    def __init__(self, name, marks,):
        self.name = name
        self.marks = marks
        self.average = 0

    def average_marks(self):
        average = sum(self.marks)/len(self.marks)
        self.average = average
        print(average)

    def get_grade(self):
        if self.average > 90:
            print('A')
        elif 60 <= self.average <= 90:
            print('B')
        else:
            print('C')
        
john = Student("John", [10,90,70]) 
john.average_marks()       
john.get_grade()