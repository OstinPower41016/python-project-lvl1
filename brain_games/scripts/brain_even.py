from random import randint
import prompt
from brain_games.cli import get_user_name


def game_iter():
    """
    :return: returns true if the answer is correct otherwise
    """

    random_number = randint(1, 100)
    print(f'Question: {random_number}')
    answer_user = prompt.string('Your answer: ')
    right_answer = 'yes' if random_number % 2 == 0 else 'no'
    if right_answer == answer_user:
        print('Correct!')
        return True
    else:
        print(f"{answer_user} is wrong answer ;(. "
              f"Correct answer was {right_answer}.")
        return False


def main():
    print('Welcome to the Brain Games!')
    name = get_user_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 1
    while count <= 3:
        if not game_iter():
            break
        if count == 3:
            print(f'Congratulations, {name}!')
        count += 1


if __name__ == '__main__':
    main()
