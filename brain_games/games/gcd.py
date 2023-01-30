from math import gcd
from random import randint

DISCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_game_data():
    num1 = randint(1, 50)
    num2 = randint(1, 50)
    question = f'{str(num1)} {str(num2)}'
    correct_answer = str(gcd(num1, num2))

    return question, correct_answer
