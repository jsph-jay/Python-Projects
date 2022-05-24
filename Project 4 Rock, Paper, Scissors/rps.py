import random


def play():
    user = input(
        " Pick Rock, Paper or Scissor - 'r' for rock, 'p' for paper and 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Its a tie'

    # r>s, p>r, s>p
    if is_win(user, computer):
        return 'You beat the computer'

    return 'You lost'


def is_win(player, opponent):
    # this function will return true if the player wins
    # r>s, p>r, s>p
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
        # this highlights that the player has won the rock paper scissors game


print(play())
