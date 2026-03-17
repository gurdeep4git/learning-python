grades = {}

def add_grade(student, grade):
    if student not in grades:
        grades[student] = []

    grades[student].append(grade)    


