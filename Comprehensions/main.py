nums = [3, 6, 8, 1, 9, 2, 10]
# squares = []
# for n in my_nums:
#     squares.append(n**2)


squares = [x**2 for x in nums]
print(squares)    

evens = [x for x in nums if x%2==0]
print(evens)

words = ["python", "java", "react", "node"]
uppers = [x.upper() for x in words]
print(uppers)

#Replace negative numbers with 0
nums = [3, -2, 5, -7, 8]
# value if condition else value
withZeros = [0 if x < 0 else x for x in nums]
print(withZeros)

#Get length of each word
words = ["apple", "banana", "kiwi", "mango"]
lengths = [len(x) for x in words]
print(lengths)

# Extract numbers greater than 10
nums = [4, 12, 7, 18, 3, 25]
greaterThan10 = [x for x in nums if x > 10]
print(greaterThan10)