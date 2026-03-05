with open("file.txt", mode="w") as f:
    content = "This is a sample text."
    f.write(content)

with open("file.txt", mode="r") as f:
    content = f.read()
    print(content)