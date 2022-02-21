from random import randint, choice
import brain_games.cli as cli
from brain_games.scripts.brain_games import loop


def game_iter():
    """
    :return: returns true if the answer is correct otherwise return
    tuple, when first argument is right answer and second is answer_user
    """

    def get_random_nod_number():
        first_number_rand = randint(2, 50)
        nods_first = [x for x in range(2, first_number_rand + 1)
                      if first_number_rand % x == 0]
        second_number_rand = choice(nods_first)
        nods_result = [x for x in nods_first if second_number_rand % x == 0]

        return first_number_rand, second_number_rand, nods_result

    first_number, second_number, nods = get_random_nod_number()

    answer_user = cli.ask_question(f'{first_number} {second_number}')

    if answer_user in nods:
        return True, nods[-1], answer_user
    else:
        return False, nods[-1], answer_user


def main():
    cli.print_welcome_message()
    name = cli.get_user_name()
    cli.print_rules_of_game("Find the greatest common"
                            " divisor of given numbers.")
    loop(game_iter, name)


if __name__ == '__main__':
    main()
