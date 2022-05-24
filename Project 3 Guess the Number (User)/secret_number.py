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


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high
        feedback = input(
            f'Is {guess} too high (H) or too low (L) or correct (C)?:').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low == guess + 1
    print(
        f'The computer has guessed your number correctly - the number was {guess}')


computer_guess(20)
