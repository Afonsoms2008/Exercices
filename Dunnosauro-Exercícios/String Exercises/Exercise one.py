string1 = input("Insert your desired word: ")
string2 = input("Insert the desired word to be compared with the previous word: ")

print(f"string 1: {string1}")
print(f"String 2: {string2}")
print(f"Size of String 1: {len(string1)} characters")
print(f"Size of String 2: {len(string2)} characters")
if string1.lower().strip() == string2.lower().strip:
    print("Both strings are the same!")
else:
    print("The strings are not the same!")
if len(string1) == len(string2):
    print("Both strings have the same size!")
else:
    print("The strings don't have the same size")