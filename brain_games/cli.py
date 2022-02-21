import prompt


def get_user_name():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def print_welcome_message():
    print('Welcome to the Brain Games!')


def ask_question(expression):
    answer_user = prompt.string(f'Question {expression} ')
    print(f'Your answer: {answer_user}')
    return int(answer_user) if answer_user.lstrip("-").isdigit() \
        else answer_user


def print_rules_of_game(str=None):
    if str:
        print(str)
    else:
        print('Answer "yes" if the number is even, otherwise answer "no".')
