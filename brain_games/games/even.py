from random import randint

DISCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_data():
    question = randint(1, 100)

    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
