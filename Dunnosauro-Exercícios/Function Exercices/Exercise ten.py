import random

def crabs():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    roll = dice1 + dice2
    print(roll)
    if roll in (7,11):
        print("You are a natural, you won!")
    elif roll in (2,3,12):
        print("Craps! you lost")
    else:
        point = roll
        while True:
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            roll = dice1 + dice2
            print(roll)
            if roll == point:
                print("You WON!")
                break
            elif roll == 7:
                print("OH NO a 7... You lost.")
                break
crabs()