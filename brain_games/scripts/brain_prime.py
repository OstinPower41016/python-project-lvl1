import brain_games.cli as cli
from random import randint
from brain_games.scripts.brain_games import loop


def is_prime(n):
    if n == 1:
        return "yes"
    divider = 2
    while divider < n:
        if n % divider == 0:
            return "no"
        divider += 1
    return "yes"


def game_iter():
    rand_int = randint(1, 100)
    user_answer = cli.ask_question(rand_int)
    right_answer = is_prime(rand_int)

    if user_answer == right_answer:
        return True, right_answer, user_answer
    return False, right_answer, user_answer


def main():
    cli.print_welcome_message()
    name = cli.get_user_name()
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    loop(game_iter, name)
