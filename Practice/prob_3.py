# Given a list of numbers, find the sum and average.
 
numbers = [10,20,30]
choice = int(input("1: Sum, 2: Average: "))
if(choice == 1):
    sum = 0
    for n in numbers:
        sum= sum + n

    print("Sum is", sum)
else:
    average = 0
    sum = 0
    for n in numbers:
        sum = sum + n
        
    average = sum/len(numbers)
    print("Average is", average)





