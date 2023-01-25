#!/usr/bin/env python3
import prompt
from random import randint

from brain_games.cli import welcome_user


def brain_even(name):
    game_count = 3
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while game_count > 0:
        random_num = randint(1, 100)
        print(f'Question: {random_num}')
        user_answer = prompt.string('Your answer: ')

        if random_num % 2 == 0 and user_answer == 'yes' \
                or random_num % 2 != 0 and user_answer == 'no':
            print('Correct!')
            game_count -= 1
        else:
            if random_num % 2 == 0:
                correct_answer = 'yes'
            else:
                correct_answer = 'no'
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
                f"\nLets try again, {name}!")
            break

        if game_count == 0:
            print(f'Congratulations, {name}!')


def main():
    brain_even(welcome_user())


if __name__ == '__main__':
    main()
