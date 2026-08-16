import string
string_input = input("Insert a word/sentence to check for palindrome: ")
string_reverse = string_input[::-1]
clean_string = ""
clean_string_reverse = ""
symbols = string.punctuation
for char in string_input:
    if char not in symbols and char != " ":
        clean_string += char
for char in string_reverse:
    if char not in symbols and char != " ":
        clean_string_reverse  +=char
if clean_string == clean_string_reverse:
    print("The word/sentence is a palindrome!")
else:
    print(f"The word/sentence is not a palindrome {clean_string} is not equal to {clean_string_reverse}")