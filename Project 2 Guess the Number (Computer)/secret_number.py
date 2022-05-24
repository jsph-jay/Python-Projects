import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        # This casts this input as an integer to make it line up with the number we are guessing
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess < random_number:
            print('Guess again - You are too low')
        elif guess > random_number:
            print('Guess again -  You are too high')
    print(
        f'You have guessed the right number - the number was {random_number} -  Well Done')


guess(50)
