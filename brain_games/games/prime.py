from random import randint

DISCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game_data():
    nums = []
    question = randint(2, 1000)

    for number in range(2, 1000):
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            nums.append(number)

    if question in nums:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
