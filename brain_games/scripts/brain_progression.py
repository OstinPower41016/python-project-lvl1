import brain_games.cli as cli
from random import randint
from brain_games.scripts.brain_games import loop


def game_iter():
    start_number = randint(1, 50)
    step = randint(2, 10)
    range_output_data = randint(5, 10)
    missing_number_position = randint(2, range_output_data)
    generate_numbers = [x * step for x in
                        range(start_number,
                              start_number + range_output_data + 1)]
    right_answer = generate_numbers[missing_number_position]
    generate_numbers[missing_number_position] = ".."
    generate_numbers = [str(val) for val in generate_numbers]
    user_answer = cli.ask_question(" ".join(generate_numbers))
    if user_answer == right_answer:
        return True, right_answer, user_answer
    return False, right_answer, user_answer


def main():
    cli.print_welcome_message()
    name = cli.get_user_name()
    print("What number is missing in the progression?")
    loop(game_iter, name)


a = [x for x in range(10)]
a[0] = 10
