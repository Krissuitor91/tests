import random
active = True
num = random.randrange(1, 101)

while active:
    guess = int(input('Guess the number between 1 and 100: '))
    if guess > num:
        print('Lower!')
    elif guess < num:
        print('Higher!')
    elif guess == num:
        print('Correct!')
        num = random.randrange(1, 101)
