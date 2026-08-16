name = input("Insert your name: ")
inverted_stair = ""
inverted_stair += name
iteration = len(name) +1
for _ in name:
    iteration -= 1
    print(name[:iteration])
    