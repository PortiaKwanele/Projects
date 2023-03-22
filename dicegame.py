import random

def roll_dice():
    """Roll two dice and return the sum of their values."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

print("Let's play a dice game!")
input("Press enter to roll the dice...")

sum_of_dice = roll_dice()
print("You rolled a", sum_of_dice)

if sum_of_dice == 7 or sum_of_dice == 11:
    print("You win!")
elif sum_of_dice == 2 or sum_of_dice == 3 or sum_of_dice == 12:
    print("You lose!")
else:
    print("Roll again until you get the same value or a 7...")

    point = sum_of_dice
    sum_of_dice = roll_dice()
    print("You rolled a", sum_of_dice)

    while sum_of_dice != point and sum_of_dice != 7:
        sum_of_dice = roll_dice()
        print("You rolled a", sum_of_dice)

    if sum_of_dice == point:
        print("You win!")
    else:
        print("You lose!")
