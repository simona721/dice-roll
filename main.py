import random

MIN_VALUE = 1
MAX_VALUE = 6

roll_dice = "yes"

while roll_dice == "yes":
    print("Rolling dice: ")
    print(random.randint(MIN_VALUE, MAX_VALUE))
    print(random.randint(MIN_VALUE, MAX_VALUE))
    
    roll_dice = input("Do you want to roll the dice again? ")
        