import random
from os import system

roll = "yes"

while roll == 'yes' or roll == 'y':
    system('cls')
    print("Rolling the dices...")
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    print("The values are:")
    print(f"{dice_1}\nand\n{dice_2}")

    roll = str(input("You want to roll again?\n"))
