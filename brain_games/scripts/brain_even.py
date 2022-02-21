from random import randint
import brain_games.cli as cli
from brain_games.scripts.brain_games import loop


def game_iter():
    """
    :return: returns true if the answer is correct otherwise return
    tuple, when first argument is right answer and second is answer_user
    """

    random_number = randint(1, 100)
    answer_user = cli.ask_question(random_number)
    right_answer = 'yes' if random_number % 2 == 0 else 'no'
    if right_answer == answer_user:
        return True, right_answer, answer_user
    else:
        return False, right_answer, answer_user


def main():
    cli.print_welcome_message()
    name = cli.get_user_name()
    cli.print_rules_of_game()
    loop(game_iter, name)


if __name__ == '__main__':
    main()
