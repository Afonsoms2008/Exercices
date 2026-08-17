import random
with open("Words-for-programs.txt", "r" , encoding="utf-8") as file:
    words = file.readlines()
word = random.choice(words).lower().strip()
letters = list(word)
random.shuffle(letters)
word_shuffled = "".join(letters)

print(f"The shuffled word is {word_shuffled}!")
guessed = False
for _ in range(6):
    guess = input("Insert the word you think was shuffled: ").lower().strip()
    if guess == word:
        print("You Won!")
        guessed = True
    else:
        print("Wrong! try again")
if not guessed:
    print(f"You lost! The word was {word}")
