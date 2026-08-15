import random
def randomizer(string):
    chars = list(string)
    random.shuffle(chars)
    randomized = "".join(chars)
    randomized = randomized.lower()
    return randomized

word = input("Insert the word to be randomized: ")
randomized_word = randomizer(word)
print(randomized_word)