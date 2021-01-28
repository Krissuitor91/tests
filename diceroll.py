import random

active = True

def dice_roll(m):
    res = random.randrange(1, m)
    print(res)

while active:
    dice_input = input('Number of dice: ')
    value_input = input('Maximum value: ') 
    dice = int(dice_input)
    m = int(value_input) + 1
    for i in range(1, dice + 1):
        dice_roll(m)
