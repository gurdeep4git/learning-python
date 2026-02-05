# Count how many times a character appears in a string.

sentence = "I am a string"
count = 0
try:
    character = input("Enter a char to count:")
    
    if character.isdigit():
        raise ValueError("Please enter a char not number")
    
    for x in sentence:
        if(x == character):
            count = count + 1

    print(f"{character} count is {count}")
except Exception as e:
    print("Exception", e)


