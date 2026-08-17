import random
with open("Words-for-programs.txt", "r", encoding="utf-8") as file:
    word_list = file.readlines()
word = random.choice(word_list).strip().lower()

life = 6
hang = ["-"] * len(word)
while True:
    letter = input("Insert the letter: ").strip().lower()
    found = False
    for i, char in enumerate(word):
        if letter == char:
            hang[i] = letter
            found = True
            print(hang)
        print(f"{letter} is in the hang good work!")
    if not found:
        life -= 1
        print(F"{letter} is not part of the word! {life} life remaining")
        print(hang)
    if life == 0:
        print(hang)
        print("You lost!")
        break
    if "".join(hang) == word:
        print(hang)
        print("You won!")
        break
    
    