#!/use/local/bin/env python
from brain_games.cli import get_user_name


def main():
    print("Welcome to the Brain Games!")
    get_user_name()


def loop(func, name):
    count = 1

    while count <= 3:
        is_correct_answer, right_answer, answer_user = func()
        if not is_correct_answer:
            print(f"{answer_user} is wrong answer ;(."
                  f" Correct answer was {right_answer}.")
            print(f"Let's try again, {name}!")
            break
        if count == 3:
            print(f'Congratulations, {name}!')
            break
        count += 1
        print('Correct!')


if __name__ == "__main__":
    main()
