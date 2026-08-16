VOWELS = ("a","e","i","o","u")
blank = " "
sentence = input("Insert a sentence: ").lower()
vowel_count = 0
blank_count = 0
for char in sentence:
    if char in VOWELS:
        vowel_count += 1
    elif char == blank:
        blank_count +=1

print(f"The sentence has {vowel_count} vowels and {blank_count} spaces")
