import prompt
from brain_games.cli import welcome_user

GAME_COUNT = 3


def launch_game(game):
    name = welcome_user()
    print(game.DISCRIPTION)
    count = 0

    while count < GAME_COUNT:
        question, correct_answer = game.get_game_data()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            count += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
                f"\nLets try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
