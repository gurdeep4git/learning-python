def remove_duplicates(arr):
    uniques = []
    
    for x in arr:
        if x not in uniques:
            uniques.append(x)
    
    print(uniques)


remove_duplicates([1,2,2,3,4,4])

def count_frequency(arr):
    result = {}
    for x in arr:
        if x in result:
            result[x] = result[x] + 1
        else:
            result[x] = 1

    print(result)        

count_frequency(["apple","banana","apple","orange"])
