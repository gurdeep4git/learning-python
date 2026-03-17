from school.students import list_students

def print_students():
    students = list_students()

    for x in students:
        print(x)