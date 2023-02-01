from random import randint, choice

DISCRIPTION = 'What number is missing in the progression?'


def get_game_data():
    question = [str(i) for i in range(randint(1, 50), 500, randint(2, 10))][:10]
    correct_answer = choice(question)
    index = question.index(correct_answer)
    question[index] = '..'
    question = ' '.join(question)

    return question, correct_answer
