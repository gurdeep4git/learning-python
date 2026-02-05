# Given a list, remove duplicate elements.

# numbers = [1, 2, 3, 2, 4, 5, 1]
# uniques = []
# seen = set()

# for n in numbers:
#     if n not in seen:
#         uniques.append(n)
#         seen.add(n)

# print(f"Unique numbers", uniques)      

# Given a list, print only the elements that appear more than once.
numbers = [1, 2, 3, 2, 4, 5, 1]
duplicates = []
seen = set()
added = set()

for n in numbers:
    if n not in seen:
        seen.add(n)
    elif n not in added:
        duplicates.append(n)
        added.add(n)

print(f"Unique numbers", duplicates) 


