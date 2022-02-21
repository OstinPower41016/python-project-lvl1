import brain_games.cli as cli
from random import randint, choice
from brain_games.scripts.brain_games import loop

OPERATORS = ["+", "-", "*"]


def game_iter():
    one, second = (randint(1, 50), randint(1, 50))
    operator = choice(OPERATORS)
    answer_user = cli.ask_question(f"{one} {operator} {second}")
    right_answer = eval(f"{one}{operator}{second}")
    return right_answer == answer_user


def main():
    cli.print_welcome_message()
    name = cli.get_user_name()
    print("What is the result of the expression?")
    loop(game_iter, name)
