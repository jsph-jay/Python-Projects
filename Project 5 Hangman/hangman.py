import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 10

    # GETTING USER INPUT
    while len(word_letters) > 0 and lives > 0:
        # letters already used

        print('You have', lives, ' lives left and these are the letters Already Used:', ''.join(
            used_letters))

        # what the current word is with -
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # taking away a life
                print('Letter is not in the word - Try Again')

        elif user_letter in used_letters:
            print('You have already used this letter - Pick Again')

        else:
            print('Invalid Character - Pick Again')
    # gets here when len(word_letters)==0 or when they have died
    if lives == 0:
        print('Game Over - The Word Was', word)
    else:
        print('You have guessed the word', word,)


#user_input = input('Type Something: ')
# print(user_input)
hangman()
