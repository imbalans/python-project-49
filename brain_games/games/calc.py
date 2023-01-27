from random import randint, choice

DISCRIPTION = 'What is the result of the expression?'


def get_game_data():
    char = choice('+-*')
    num1 = randint(10, 20)
    num2 = randint(1, 9)
    question = f'{str(num1)} {char} {str(num2)}'

    if char == '+':
        correct_answer = str(num1 + num2)
    elif char == '-':
        correct_answer = str(num1 - num2)
    else:
        correct_answer = str(num1 * num2)

    return question, correct_answer
