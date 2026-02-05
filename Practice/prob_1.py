# Write a program to take a number and print its square and cube.

def calc():
    try:
        number = float(input("Enter a number:"))
        if number.is_integer():
            number = int(number)

        print(f"Square is {number ** 2}")
        print(f"Cube is {number ** 3}")
        
    except Exception as e:
        print("Please enter a valid number", e)    


calc()        


    