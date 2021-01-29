
'''
* File Name : random_game.py

* Language : Python

* Creation Date : 05-01-2021

* Last Modified : Wed Jan  6 22:46:12 2021

* Created By : David Hanson

'''

from random import randint


def run_guess(guess, answer):
    try:
        if 1 <= int(guess) <= 10:
            if int(guess) == int(answer):
                print('Way to go!')
                return True
            else:
                print("Nope, you're dumb, please try again.")
                return False
        else:
            print('No, within the range please.')
            return False
    except ValueError as err:
        return err


if __name__ == '__main__':
    random_number = randint(1, 10)
    while True:
        try:
            from_input = int(input('Guess a number between 1 and 10: '))
            if run_guess(from_input, random_number):
                break
        except ValueError:
            print("Please enter a number.")
            continue
